# url.py (the url configuration)

from django.conf.urls.defaults import *
from django.conf.urls import patterns;

import views;

urlpatterns = patterns('',
    (r'^latest/$', views.latest_books),
)

                
