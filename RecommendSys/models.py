from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    c_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        # 通过app_label来指定要使用的数据库
        # 需指定db_table，否则该class的表名会是mysql_animal
        # 如果不指定Meta的app_label，会使用默认数据库
        ordering = ['c_time']


class AuthorCollectField(models.Model):
    username = models.CharField(max_length=255)
    fieldid = models.PositiveIntegerField()
    fieldname = models.CharField(max_length=200)
    fieldcount = models.PositiveIntegerField()
    
    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['username', '-fieldcount']

class PaperCollectField(models.Model):
    username = models.CharField(max_length=255)
    fieldid = models.PositiveIntegerField()
    fieldname = models.CharField(max_length=200)
    fieldcount = models.PositiveIntegerField()
    
    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['username', '-fieldcount']

class AuthorCollect(models.Model):
    username = models.CharField(max_length=255)
    authorid = models.PositiveIntegerField()
    authorname = models.CharField(max_length=255)
    authoraffiliation = models.CharField(max_length=255)
    c_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['username','c_time']

class PaperCollect(models.Model):
    username = models.CharField(max_length=255)
    paperid = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    authors = models.CharField(max_length=255)
    abstract = models.TextField()
    c_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['username','c_time']

class AffiliationCollect(models.Model):
    username = models.CharField(max_length=255)
    affiliationid = models.PositiveIntegerField()
    affiliationname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    introduction = models.TextField()
    url = models.CharField(max_length=500)
    c_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['username','c_time']

class ParsedAffiliations(models.Model):
    affiliationid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    shortname = models.CharField(max_length=20)
    countryname = models.CharField(max_length=255)
    introduction = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['affiliationid']

class RecommendResult(models.Model):
    username = models.CharField(max_length=255)
    affiliationshortname = models.CharField(max_length=20)
    needupdate = models.BooleanField()
    authorid0 = models.PositiveIntegerField()
    authorid1 = models.PositiveIntegerField()
    authorid2 = models.PositiveIntegerField()
    authorid3 = models.PositiveIntegerField()
    authorid4 = models.PositiveIntegerField()
    authorid5 = models.PositiveIntegerField()
    authorid6 = models.PositiveIntegerField()
    authorid7 = models.PositiveIntegerField()
    authorid8 = models.PositiveIntegerField()
    authorid9 = models.PositiveIntegerField()

    def __str__(self):
        return (self.username, self.affiliationshortname)

    class Meta:
        ordering = ['username', 'affiliationshortname'] 


class CUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class CUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class CUTeAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class CUTeParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class ECNUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class ECNUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class FUDANAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class FUDANParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class HUSTAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class HUSTParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class LONDONAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class LONDONParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class MITAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class MITParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class NJUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class NJUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class NTUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class NTUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class PKUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class PKUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SCUTAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SCUTParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SEUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SEUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SJTUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SJTUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SYSUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SYSUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SZUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class SZUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class THUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class THUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class TONGJIAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class TONGJIParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class UTAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class UTParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class WHUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class WHUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class ZJUAuthorField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    field_id1 = models.PositiveIntegerField()
    weight1 = models.FloatField()
    field_id2 = models.PositiveIntegerField()
    weight2 = models.FloatField()
    field_id3 = models.PositiveIntegerField()
    weight3 = models.FloatField()
    field_id4 = models.PositiveIntegerField()
    weight4 = models.FloatField()
    field_id5 = models.PositiveIntegerField()
    weight5 = models.FloatField()

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']

class ZJUParentField(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    parents = models.CharField(max_length=300)

    def __str__(self):
        return self.author_id

    class Meta:
        ordering = ['author_id']




class AmPaper(models.Model):
    paper_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=2500)
    doi = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    doc_type = models.PositiveIntegerField()
    date = models.DateField(blank=True, null=True)
    journal_id = models.PositiveIntegerField()
    conference_series_id = models.PositiveIntegerField()
    conference_instance_id = models.PositiveIntegerField()
    volume = models.SmallIntegerField()
    issue = models.SmallIntegerField()
    first_page = models.SmallIntegerField()
    last_page = models.SmallIntegerField()
    created_at = models.PositiveIntegerField()
    updated_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'am_paper'

class AmPaperAuthor(models.Model):
    paper_id = models.PositiveIntegerField()
    author_id = models.PositiveIntegerField()
    affiliation_id = models.PositiveIntegerField()
    sequence = models.PositiveSmallIntegerField()
    created_at = models.PositiveIntegerField()
    updated_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'am_paper_author'

class AmAuthor(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    normalizedname = models.CharField(db_column='NormalizedName', max_length=255)  # Field name made lowercase.
    name_cn = models.CharField(max_length=500)
    last_known_affiliation_id = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()
    updated_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'am_author'

class AmAffiliation(models.Model):
    affiliation_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    name_cn = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    wiki_page = models.CharField(max_length=500)
    country_id = models.IntegerField()
    grid_id = models.CharField(max_length=100)
    introduction = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.PositiveIntegerField()
    updated_at = models.PositiveIntegerField()
    wikidata = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'am_affiliation'

class AmPaperAbstract(models.Model):
    paper_id = models.PositiveIntegerField(primary_key=True)
    abstract = models.TextField()
    created_at = models.PositiveIntegerField()
    updated_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'am_paper_abstract'

class AmCountry(models.Model):
    country_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_cn = models.CharField(max_length=255)
    official_name = models.CharField(max_length=255)
    alpha2 = models.CharField(max_length=2)
    alpha3 = models.CharField(max_length=3)
    numeric = models.CharField(max_length=3)
    independence = models.IntegerField()
    continent = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'am_country'

class AmPaperField(models.Model):
    paper_id = models.PositiveIntegerField()
    score = models.FloatField()
    keyword = models.CharField(max_length=255)
    field_id = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'am_paper_field'

class AmField(models.Model):
    field_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    name_cn = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    level = models.PositiveIntegerField()
    wiki_page = models.CharField(max_length=500)
    introduction = models.TextField()
    created_at = models.PositiveIntegerField()
    updated_at = models.PositiveIntegerField()
    wikidata = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'am_field'