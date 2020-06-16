from RecommandSys.models import *


def get_field_distribution_by_paper(paper_id):
    field_ids = AmPaperField.objects.using("remotedb").filter(paper_id=paper_id).values_list("field_id")
    return [field_id[0] for field_id in field_ids]

def get_field_distribution_by_author(author_id):
    paper_ids = AmPaperAuthor.objects.using("remotedb").filter(author_id=author_id).values_list("paper_id")
    field_dist = {}
    for paper_id in paper_ids:
        tmp = get_field_distribution_by_paper(paper_id[0])
        for field_id in tmp:
            if field_id in field_dist:
                field_dist[field_id] += 1
            else :
                field_dist[field_id] = 1
    return field_dist

def get_field_distribution_of_user(username):
    pcf = PaperCollectField.objects.filter(username=username).values_list("fieldid", "fieldcount")
    acf = AuthorCollectField.objects.filter(username=username).values_list("fieldid", "fieldcount")
    dist = {}
    max_count = 0
    for id, count in pcf:
        if id in dist:
            dist[id] += count
        else:
            dist[id] = count
        max_count = max(max_count, dist[id])
    
    for id, count in acf:
        if id in dist:
            dist[id] += count
        else:
            dist[id] = count
        max_count = max(max_count, dist[id])
    result = []
    for id, count in dist.items():
        result.append((id, count/max_count))
    return result
    