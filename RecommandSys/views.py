from django.shortcuts import render, redirect
from RecommandSys.models import *
from RecommandSys.get_field import *
from RecommandSys.get_recommend import *
import hashlib
from django.contrib import messages
from django.http import JsonResponse
import json
import time
from FinalProject.settings import FIELD_MAP

# Create your views here.

def hash_code(s, salt='RecommandSystem'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def login(request):
    if request.session.get("islogin", None):
        return redirect('/home/')
    if request.is_ajax():
        if request.method == "POST":
            jsdata = {"iserror": False}
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            try:
                user = UserInfo.objects.get(username=username)
                if user.password == hash_code(password):
                    request.session['islogin'] = True
                    request.session['userid'] = user.id
                    request.session['username'] = user.username
                    return JsonResponse(jsdata)
                else:
                    jsdata["iserror"] = True
                    jsdata["error"] = "wrong password"
                    return JsonResponse(jsdata)
            except:
                jsdata["iserror"] = True
                jsdata["error"] = "User does not exist"
                return JsonResponse(jsdata)
            jsdata["iserror"] = True
            jsdata["error"] = "Please check the content"
            return JsonResponse(jsdata)
    return render(request, 'login/login.html', locals())

def register(request):
    if request.session.get('islogin', None):
        return redirect("/home/")
    if request.is_ajax():
        if request.method == "POST":
            jsdata = {"iserror": False}
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            same_name_user = UserInfo.objects.filter(username=username)
            # print(same_name_user)
            if same_name_user:
                jsdata["iserror"] = True
                jsdata["error"] = "User already exists, please re-select username"
                return JsonResponse(jsdata)
            new_user = UserInfo.objects.create(username=username, password=hash_code(password))
            return JsonResponse(jsdata)
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('islogin', None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')

def home(request):
    if not request.session.get('islogin', None):
        return redirect('/login/')
    username = request.session["username"]
    pcf = PaperCollectField.objects.filter(username=username).values_list("fieldname", "fieldcount")
    acf = AuthorCollectField.objects.filter(username=username).values_list("fieldname", "fieldcount")
    pcf = pcf[:min(10,len(pcf))]
    acf = acf[:min(10,len(acf))]
    ispcf = False
    isacf = False
    acfd = []
    pcfd = []
    max1 = max2 = 0
    if pcf:
        ispcf = True
        for fieldname, count in pcf:
            pcfd.append({"value": count,"name": fieldname})
            max1 = max(max1, count)
    
    if acf:
        isacf = True
        for fieldname, count in acf:
            acfd.append({"value": count,"name": fieldname})
            max2 = max(max2, count)

    return render(request, 'home/home.html', {"username": username, "pcfd": json.dumps(pcfd), "acfd": json.dumps(acfd), "max1": max1, "max2": max2, "ispcf": ispcf, "isacf": isacf})

def paper(request):
    username = request.session["username"]
    collects = PaperCollect.objects.filter(username=username).values_list("title", "authors", "year", "abstract")
    papers = []
    for title, authors, year, abstract in collects:
        authors = authors.split(",")
        papers.append({"title": title, "authors": authors, "year":year, "abstract": abstract})
    return render(request, 'home/paper.html', {"Search": "papersearch", "username": username, "papers": papers})

def papersearch(request):
    if request.is_ajax():
        if request.method == "POST":
            jsdata = {"iserror": False}
            username = request.session['username']
            paperid = int(request.POST.get('paperid', None))
            year = int(request.POST.get('year', None))
            title = request.POST.get('title', None)
            authors = request.POST.get('authors', None)
            abstract = request.POST.get('abstract', None)
            samecollect = PaperCollect.objects.filter(username=username, paperid=paperid)
            if samecollect:
                jsdata["iserror"] = True
                jsdata["message"] = "The paper has been collected"
            else :
                new_collect = PaperCollect.objects.create(username=username, paperid=paperid, year=year, title=title, authors=authors, abstract=abstract)
                field_ids = get_field_distribution_by_paper(paperid)
                for field_id in field_ids:
                    field_name = AmField.objects.using("remotedb").get(field_id=field_id).name
                    tmp = PaperCollectField.objects.filter(username=username, fieldid=field_id)
                    print(tmp)
                    if tmp:
                        tmp[0].fieldcount += 1
                        tmp[0].save()
                    else:
                        new_field = PaperCollectField.objects.create(username=username, fieldid=field_id, fieldname=field_name, fieldcount=1)
                recom = RecommendResult.objects.filter(username=username)
                if recom:
                    recom.update(needupdate = True)
            return JsonResponse(jsdata)
            
    results = []
    if request.method == "GET":
        papername = request.GET.get("name")        
        print("search for paper ", papername)  
        am_paper = AmPaper.objects.using("remotedb").filter(title__icontains=papername).values_list("paper_id","title", "year")[:16]
        for paperid, title, year in am_paper:
            abstract = AmPaperAbstract.objects.using("remotedb").filter(paper_id=paperid).values_list("abstract")
            if not abstract:
                abstract=""
            else :
                abstract = abstract[0][0]
            au_aff_ids = AmPaperAuthor.objects.using("remotedb").filter(paper_id=paperid).values_list("author_id", "affiliation_id")
            authors = []
            affiliations = []
            affiliationids_searched = []
            for authorid, affiliationid in au_aff_ids:
                authors.append(AmAuthor.objects.using("remotedb").get(author_id=authorid).name)
                if affiliationid != 0 and affiliationid not in affiliationids_searched:
                    affiliations.append(AmAffiliation.objects.using("remotedb").get(affiliation_id=affiliationid).name)
                    affiliationids_searched.append(affiliationid)
            results.append({"paperid":paperid, "title": title, "year": year, "authors": authors, "affiliations": affiliations, "abstract": abstract})
            
    return render(request, 'home/paper.html', {"Search": "papersearch", "issearch": True, "username": request.session["username"], "results": results})

def author(request):
    username = request.session["username"]
    collects = AuthorCollect.objects.filter(username=username).values_list("authorname", "authoraffiliation")
    authors = []
    for authorname, authoraffiliation in collects:
        authors.append({"authorname": authorname, "authoraffiliation": authoraffiliation})
    print(authors)
    return render(request, 'home/author.html', {"Search": "authorsearch", "username": username, "authors": authors})

def authorsearch(request):
    if request.is_ajax():
        if request.method == "POST":
            jsdata = {"iserror": False}
            username = request.session['username']
            authorid = int(request.POST.get('authorid', None))
            affiliation = request.POST.get('affiliation', None)
            name = request.POST.get('name', None)
            samecollect = AuthorCollect.objects.filter(username=username, authorid=authorid)
            if samecollect:
                jsdata["iserror"] = True
                jsdata["message"] = "The author has been collected"
            else :
                new_collect = AuthorCollect.objects.create(username=username, authorid=authorid, authorname=name, authoraffiliation=affiliation)
                field_dist = get_field_distribution_by_author(authorid)
                for field_id, count in field_dist.items():
                    field_name = AmField.objects.using("remotedb").get(field_id=field_id).name
                    tmp = PaperCollectField.objects.filter(username=username, fieldid=field_id)
                    if tmp:
                        tmp[0].fieldcount += count
                        tmp[0].save()
                    else:
                        new_field = AuthorCollectField.objects.create(username=username, fieldid=field_id, fieldname=field_name, fieldcount=count)
                recom = RecommendResult.objects.filter(username=username)
                if recom:
                    recom.update(needupdate = True)
            return JsonResponse(jsdata)
            
    results = []
    if request.method == "GET":
        authorname = request.GET.get("name")  
        print("search for author ", authorname)      
        am_author = AmAuthor.objects.using("remotedb").filter(name__icontains=authorname).values_list('author_id','name', "normalizedname", "last_known_affiliation_id")[:26]
        for author_id, name, normalizedname, last_known_affiliation_id in am_author:
            affiliation = ""
            if last_known_affiliation_id:
                affiliation = AmAffiliation.objects.using("remotedb").get(affiliation_id=last_known_affiliation_id).name
            results.append({"authorid":author_id, "name": name, "normalizedname": normalizedname, "affiliation":affiliation})
    return render(request, 'home/author.html', {"Search": "authorsearch", "issearch": True, "username": request.session["username"], "results": results})

def test(request):
    test = []
    return render(request, 'test.html' ,locals())

def affiliation(request):
    username = request.session["username"]
    collects = AffiliationCollect.objects.filter(username=username).values_list("affiliationid", "affiliationname", "country", "introduction", "url")
    affiliations = []
    for affiliationid, affiliationname, country, introduction, url in collects:
        affiliations.append({"name": affiliationname, "country": country, "introduction": introduction, "url":url})
    print(affiliations)
    return render(request, 'home/affiliation.html', {"Search": "affiliationsearch", "username": request.session["username"], "affiliations": affiliations})

def affiliationsearch(request):
    if request.is_ajax():
        if request.method == "POST":
            jsdata = {"iserror": False}
            username = request.session['username']
            affiliationid = int(request.POST.get('affiliationid', None))
            introduction = request.POST.get('introduction', None)
            affiliationname = request.POST.get('name', None)
            country = request.POST.get('country', None)
            samecollect = AffiliationCollect.objects.filter(username=username, affiliationid=affiliationid)
            if samecollect:
                jsdata["iserror"] = True
                jsdata["message"] = "The affiliation has been collected"
            else :
                url = AmAffiliation.objects.using("remotedb").filter(affiliation_id=affiliationid).values_list("url")[0][0]
                new_collect = AffiliationCollect.objects.create(username=username, affiliationid=affiliationid, introduction=introduction, affiliationname=affiliationname, country=country, url=url)
            return JsonResponse(jsdata)
            
    results = []
    if request.method == "GET":
        affiliationname = request.GET.get("name")  
        print("search for affiliation ", affiliationname)      
        am_affiliation = AmAffiliation.objects.using("remotedb").filter(name__icontains=affiliationname).values_list('affiliation_id','name', "country_id", "introduction")[:16]
        for affiliation_id, name, country_id, introduction in am_affiliation:
            country = ""
            if country_id:
                country = AmCountry.objects.using("remotedb").get(country_id=country_id).name
            results.append({"affiliationid":affiliation_id, "name": name, "country": country, "introduction":introduction})
    return render(request, 'home/affiliation.html', {"Search": "affiliationsearch", "issearch": True, "username": request.session["username"], "results": results})

def recommend(request):
    parsed_list = []
    pas = ParsedAffiliations.objects.all()
    for pa in pas:
        parsed_list.append({"name": pa.name, "short": pa.shortname, "country": pa.countryname, "introduction": pa.introduction})
    return render(request, 'home/recommend.html', {"username": request.session["username"], "Recommend": True, "schools": parsed_list})

def result(request):
    shortname = request.GET.get("short")
    username = request.session["username"]
    recommend = []
    try:
        recom = RecommendResult.objects.get(username=username, affiliationshortname=shortname)
        if not recom.needupdate:
            print("no update")
            for i in range(10):
                recommend.append((getattr(recom, f"authorid{i}"), 0))
                
        else:
            print("update")
            user_dist = get_field_distribution_of_user(username)
            t1 = time.time()
            recommend = get_recommend(user_dist, shortname, 10)
            print(time.time()-t1)
            recom.authorid0 = recommend[0][0]
            recom.authorid1 = recommend[1][0]
            recom.authorid2 = recommend[2][0]
            recom.authorid3 = recommend[3][0]
            recom.authorid4 = recommend[4][0]
            recom.authorid5 = recommend[5][0]
            recom.authorid6 = recommend[6][0]
            recom.authorid7 = recommend[7][0]
            recom.authorid8 = recommend[8][0]
            recom.authorid9 = recommend[9][0]
            recom.needupdate = False
            recom.save()
            
    except:
        print("no such pattern")
        user_dist = get_field_distribution_of_user(username)
        t1 = time.time()
        recommend = get_recommend(user_dist, shortname, 10)
        print(time.time()-t1)
        new_recommend = RecommendResult.objects.create(username=username, affiliationshortname=shortname, needupdate=False,
                authorid0=recommend[0][0], authorid1=recommend[1][0], authorid2=recommend[2][0], authorid3=recommend[3][0], 
                authorid4=recommend[4][0], authorid5=recommend[5][0], authorid6=recommend[6][0], authorid7=recommend[7][0],
                authorid8=recommend[8][0], authorid9=recommend[9][0])
    result = []
    for id, _ in recommend:
        author_name = AmAuthor.objects.using("remotedb").get(author_id=id).name
        author_field = eval(f"{shortname}AuthorField").objects.get(author_id=id)
        field = []
        for i in range(1,6):
            field_id = getattr(author_field, f"field_id{i}")
            weight = getattr(author_field, f"weight{i}")
            if field_id != 0:
                field.append({"value": weight, "name": FIELD_MAP[field_id]})
        result.append((author_name, json.dumps(field)))
    return render(request, 'home/result.html', {"username": username, "affiliationname": shortname, "Recommend": True, "result": result})