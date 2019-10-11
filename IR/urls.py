from django.conf.urls import patterns, include, url

from django.contrib import admin
from main.views import *
from statistics.views import *
# adding school.views
#from school.views import *
from django.contrib.auth import views

#from django.contrib.auth.views import login, logout
#from log.forms import LoginForm
#from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IR.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^IntroIR/', IntroIR),
    url(r'^Opendata/', Opendata),
    url(r'^IssueAnaly/', IssueAnaly),
    url(r'^IRdb/', IRdb),
    url(r'^Resource/', Resource),

#    url(r'^content/', content),
#    url(r'', include('log.urls')),
#    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
#    url(r'^logout/$', views.logout, {'next_page': '/login'}),
#    url(r'^accounts/login/$',login,{'template_name':'login.html'}),
#    url(r'^accounts/logout/$',logout),
    url(r'^accounts/login/$', account),
    url(r'^login/$', login),
    url(r'^apply/$', appl),
    url(r'^register/$', register),
    url(r'^validate/$', validate),
    url(r'^judge/$', judge),
#    url(r'^accounts/login/$',login,{'template_name':'login.html'},
#    url(r'^accounts/logout/$',logout),
#    url(r'^index/$',index),
#    url(r'^logout/', logout),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/'}),
    #statistics
    url(r'^statistics-enroll/$',statistics_enroll),
    url(r'^selectQuery/$',selectQuery),
    url(r'^enrollQuery/$',enrollQuery),
    url(r'^statistics-enrollmap/$' ,enrollMap),
    url(r'^IRinfo/$' ,IRinfo),
    url(r'^ldappage/$' ,ldappage),
    url(r'^ldapCheck/$' ,ldapCheck),

    url(r'^IRofficemember/$' ,IRofficemember),
    # All Documents web
    url(r'^alldocs_IRdb/$' ,alldocs_IRdb),
    url(r'^alldocs_opendata/$' ,alldocs_opendata),
    url(r'^alldocs_analy/$' ,alldocs_analy),

    #success school app
    #any school app's urls are beginning here
    # Delete all of school page, thank you Ms. making anything in vain.

    )
