# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Slide(models.Model):
    title = models.CharField(max_length=50)

class Topics(models.Model):
    category =  models.CharField(max_length=32)
    about = 'education'
    discovery = 'discovery'
    culture = 'culture'
    people = 'people'
    service ='service'
    CATA_ICON_CHOICES = (
        (about, '關於網站'),
        (discovery, '文章展覽'),
        (culture, '類別導覽'),
        (people, '文章分類'),
        (service, '作品分享')
    )
    cata_icon = models.CharField(
        max_length=32,
        choices=CATA_ICON_CHOICES,
        default=about,
    )

    Intr = '/IntroIR'
    Open = '/Opendata'
    Issu = '/IssueAnaly'
    IRdb = '/IRdb'
    Reso ='/Resource'
    CATA_NET_CHOICES = (
        (Intr, '關於網站'),
        (Open, '文章展覽'), 
        (Issu, '類別導覽'), 
        (IRdb, '文章分類'), # 根據分類百文章 (Travel, CS, language)
        (Reso, '作品分享')
    )
    cata_net = models.CharField(
        max_length=32,
        choices=CATA_NET_CHOICES,
        default=Intr,
    )

    IRDB_CATA_CHOICES = (
        ('no','無'),
        ('language', '語言相關'),
        ('itthing', '資訊那些事'),
        ('travel', '旅遊日記'),
    )
    irdb_cata = models.CharField(
        max_length=32,
        choices=IRDB_CATA_CHOICES,
        default='無',
    )
    photo = models.CharField(max_length=255, default='static/img/article_img/default.png')
    #photo = models.FileField(upload_to='static/img/article_img/',default='static/img/article_img/default.png')
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
