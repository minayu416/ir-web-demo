# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import *
from django.contrib import auth  # 別忘了import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from views import index
#from django.contrib.auth.views import login, logout  # 利用內建的view funciton
import json
import requests
import xml.etree.cElementTree as ET


# Create your views here.


#def content(request):
#    slide = Slide.objects.all()
#    slides = []
#    for s in slide:
#        dic = {}
#        dic["title"] = s.title
#        slides.append(dic)

#    slides = json.dumps(slides)

#    return HttpResponse(slides)
#    return render_to_response('content.html',RequestContext(request,{'slide':slides}))

    #Topics = Topics.objects.all()
    #return render(request, 'index.html', {
    #    'slide': jsSlide,
    #    'Topics': Topics,
    #})
#def IR_index(request):
#    Topics = Topics.objects.all()
#    return render_to_response('index.html',RequestContext(request,{'slide':jsSlide}))
#def topics(request):
#    Topics = Topics.objects.all()
#    return render_to_response('index.html',locals())
def index(request):

    if request.user.is_staff:
        topics = Topics.objects.all().order_by("-eventdate")[:10]

    else:
        topics = Topics.objects.all().exclude(cata_icon='culture').exclude(cata_icon='people').order_by("-eventdate")[:10]

    #topics = Topics.objects.filter(cata_icon='education','discovery','service').order_by("-eventdate")[:10]
    pages = Pages.objects.get(menu=0)

    return render(request, 'index.html', {
        'topics': topics,
        'pages': pages,
    })


def IntroIR(request):
    topics = Topics.objects.filter(cata_icon='education').order_by("-eventdate")[:10]
    pages = Pages.objects.get(menu=1)

    return render(request, 'IntroIR.html', {
        'topics': topics,
        'pages': pages,
    })
def Opendata(request):
    topics = Topics.objects.filter(cata_icon='discovery').order_by("-eventdate")[:10]
    pages = Pages.objects.get(menu=2)

    return render(request, 'Opendata.html', {
        'topics': topics,
        'pages': pages,
    })
@login_required
def IssueAnaly(request):
    topics = Topics.objects.filter(cata_icon='culture').order_by("-eventdate")[:10]
    pages = Pages.objects.get(menu=3)

    return render(request, 'IssueAnaly.html', {
        'topics': topics,
        'pages': pages,
    })
@login_required
def IRdb(request):
    topics = Topics.objects.filter(cata_icon='people').order_by("-eventdate")[:10]
    pages = Pages.objects.get(menu=4)

    return render(request, 'IRdb.html', {
        'topics': topics,
        'pages': pages,
    })
def Resource(request):
    topics = Topics.objects.filter(cata_icon='service').order_by("-eventdate")[:10]
    pages = Pages.objects.get(menu=5)

    return render(request, 'Resource.html', {
        'topics': topics,
        'pages': pages,
    })
def account(request):
    return render(request, 'login.html')
def login(request):
    next = request.GET.get("next", "/")

    if request.user.is_authenticated():
        return HttpResponseRedirect(next)

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    if User.objects.filter(username = username).exists():
        if ldapCheck(username, password):
            user = User.objects.get(username = username)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login(request, user)
            return HttpResponseRedirect(next)
        else:
            user = auth.authenticate(username = username, password = password)
    else:
        return HttpResponseRedirect('/apply/')

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(next)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def appl(request):
    return render(request, 'apply.html')


def register(request):
    idnumber = request.POST.get('idnumber', '')
    username = request.POST.get('username', '')
    department = request.POST.get('department', '')
    emailaddress = request.POST.get('emailaddress', '')

    try:
    #if True:
        Register.objects.create(
            idnumber = idnumber,
            username = username,
            department = department,
            emailaddress = emailaddress
            )
        #return render(request, 'Resource.html')
        return HttpResponseRedirect('/')
    except:
        return HttpResponse('eee')

def validate(request):
    register = Register.objects.filter(validate=False)
    return render(request, 'validate.html', locals())

def judge(request):
    userlist = request.POST.getlist("userlist")
    for user in userlist:
        User.objects.create_user(user)
    Register.objects.filter(idnumber__in=userlist).update(validate=True)
    return render(request, 'validate.html')

def IRinfo(request):
    return render_to_response('IRinfo.html')

def IRmember(request):
    return render_to_response('IRmember.html')

def IRofficemember(request):
    return render_to_response('IRofficemember.html')

def ldappage(request):
    pusername = request.GET.get("username")
    ppasswd = request.GET.get("password")
    result = ldapCheck(pusername, ppasswd)
    return HttpResponse(result)

def ldapCheck(pusername, ppasswd):
    return True
    # url = "" + pusername + "&ppasswd=" + ppasswd

    # response = requests.get(url)
    # r = response.content.decode('big5').encode('utf-8')
    # r = r.replace('big5', 'utf-8')
    # root = ET.fromstring(r)
    # for child in root.getiterator('{#RowsetSchema}row'):
    #     x = child.attrib
    # if x['rcode'] == "1":
    #     return True
    # else:
    #     return False

@login_required
def alldocs_IRdb(request):
    language = Topics.objects.filter(cata_icon='people',irdb_cata='language').order_by("-eventdate")
    itthing = Topics.objects.filter(cata_icon='people',irdb_cata='itthing').order_by("-eventdate")
    travel = Topics.objects.filter(cata_icon='people',irdb_cata='travel').order_by("-eventdate")
    return render(request, 'alldocs_IRdb.html', {
        'language': language,
        'itthing': itthing,
        'travel': travel,
    })

@login_required
def alldocs_opendata(request):
    pages = Pages.objects.get(menu=2)
    topics = Topics.objects.filter(cata_icon='discovery').order_by("-eventdate")
    return render(request, 'all_docs_single.html', {
        'topics': topics,
        'pages': pages,
    })

@login_required
def alldocs_analy(request):
    pages = Pages.objects.get(menu=3)
    topics = Topics.objects.filter(cata_icon='culture').order_by("-eventdate")
    return render(request, 'all_docs_single.html', {
        'topics': topics,
        'pages': pages,
    })
