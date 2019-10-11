# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Slide(models.Model):
    title = models.CharField(max_length=50)

class Topics(models.Model):
    category =  models.CharField(max_length=32)
    education = 'education'
    discovery = 'discovery'
    culture = 'culture'
    people = 'people'
    service ='service'
	#school = 'school'
    CATA_ICON_CHOICES = (
        (education, '關於IR'),
        (discovery, '公開資訊'),
        (culture, '議題分析'),
        (people, 'IR資料庫'),
        (service, '資源分享')
	#	(school, '校庫')
    )
    cata_icon = models.CharField(
        max_length=32,
        choices=CATA_ICON_CHOICES,
        default=education,
    )

    Intr = '/IntroIR'
    Open = '/Opendata'
    Issu = '/IssueAnaly'
    IRdb = '/IRdb'
    Reso ='/Resource'
    CATA_NET_CHOICES = (
        (Intr, '關於IR'),
        (Open, '公開資訊'),
        (Issu, '議題分析'),
        (IRdb, 'IR資料庫'),
        (Reso, '資源分享')
#        (Reso, '校庫')
    )
    cata_net = models.CharField(
        max_length=32,
        choices=CATA_NET_CHOICES,
        default=Intr,
    )

    IRDB_CATA_CHOICES = (
        ('','無'),
        ('enter', '入學端'),
        ('inschool', '在學端'),
        ('graduate', '畢業端'),
    )
    irdb_cata = models.CharField(
        max_length=32,
        choices=IRDB_CATA_CHOICES,
        default='無',
    )
#    cata_net = models.CharField(max_length=255)
    photo = models.FileField(upload_to='static/img/article_img/',default='static/img/article_img/default.png')
    eventdate = models.DateField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=255)
    tar_web = models.CharField(max_length=255)
    remark =  models.CharField(max_length=255,blank=True)
    def __unicode__(self):
        return u'%s' % self.title

class Pages(models.Model):
    menu = models.IntegerField(editable=False)
    #active
    #leaf
    subject = models.CharField(max_length=100)
    intro = models.TextField(max_length=500)
    #net
    def __unicode__(self):
        return u'%s' % self.subject

class Register(models.Model):
    idnumber = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    emailaddress = models.CharField(max_length=100)
    validate = models.BooleanField(default=False)
    def __unicode__(self):
        return u'%s' % self.username

class Permit(models.Model):
    accounts = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % self.accounts
