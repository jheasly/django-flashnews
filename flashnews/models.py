from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

class Participant(models.Model):
    org_name = models.CharField(max_length=100)
    org_url = models.URLField(verify_exists=False, blank=True)
    slug = models.SlugField(unique=True, max_length=100)
    category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return self.org_name
    
    class Meta:
        ordering = ['org_name']

class Emergency(models.Model):
    updated = models.BooleanField()
    testing = models.BooleanField()
    school_related = models.BooleanField()
    quick_report_id = models.IntegerField(blank=True, null=True)
    detail = models.TextField()
    media_contact = models.TextField(blank=True)
    effective_date = models.DateTimeField()
    participant = models.ForeignKey(Participant)
    
    def __unicode__(self):
        return '%s %s' % (self.effective_date.strftime('%Y-%m-%d %H:%M:%S'), self.detail)
    
    class Meta:
        get_latest_by = 'effective_date'
        ordering = ['-effective_date']
        verbose_name_plural = 'emergencies'
    
    def the_parent_category(self):
        return self.participant.category.name

class News(models.Model):
    updated = models.BooleanField()
    testing = models.BooleanField()
    school_related = models.BooleanField()
    quick_report_id = models.IntegerField(blank=True, null=True)
    headline = models.CharField(max_length=400)
    detail = models.TextField()
    media_contact = models.TextField(blank=True)
    effective_date = models.DateTimeField()
    participant = models.ForeignKey(Participant)
    
    def __unicode__(self):
        return self.headline
    
    class Meta:
        verbose_name_plural = 'news'
    
    def the_parent_category(self):
        return self.participant.category.name
