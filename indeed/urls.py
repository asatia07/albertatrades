from django.conf.urls import patterns, include, url
from django.conf import settings
import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^search_indeed/$', views.search, name='search'),
    url(r'^profiles/home', 'indeed.views.job_listing'),
]
