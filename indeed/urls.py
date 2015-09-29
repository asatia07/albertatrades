from django.conf.urls import patterns, include, url
from django.conf import settings
from scheduler import cronjobs
import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^search_indeed/$', views.search, name='search'),
    url(r'^scheduler/update_trades/$', cronjobs.update_trades, name='update_trades'),
]
