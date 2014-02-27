from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from views import *;
from books import views;

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    #using parentheses to capture data from the matched text.
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    #for root.
    url(r'^$', welcome),
    #url(r'^search-form/$', views.search_form),
    #url(r'^search/$', views.search),
    url(r'^search/$', views.onesearch),
    url(r'^contact/$', views.contact),
)
