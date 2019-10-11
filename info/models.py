from django.db import models

# Create your models here.

class Infopage(models.Model):
    pageid = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    headintro = models.TextField(max_length=255)
    depart = models.CharField(max_length=50)
    eventdate = models.DateField(auto_now=False, auto_now_add=False)
    intro = models.TextField(max_length=255)
    def __unicode__(self):
        return u'%s' % self.subject

class Article(models.Model):
    Artid = models.CharField(max_length=32)
    title = models.CharField(max_length=32, blank=True)
    content = models.TextField(max_length=255)
    def __unicode__(self):
        return u'%s' % self.subject

class Table(models.Model):
    memberid = models.CharField(max_length=32)
    name = models.CharField(max_length=100)
    jobname = models.TextField(max_length=255)
    work = models.TextField(max_length=255)
    def __unicode__(self):
        return u'%s' % self.subject

class Photo(models.Model):
    photoid = models.CharField(max_length=32)
    description = models.TextField(max_length=255, blank=True)
    photo = models.FileField(upload_to='static/img/IRinfo/')
    def __unicode__(self):
        return u'%s' % self.subject       
