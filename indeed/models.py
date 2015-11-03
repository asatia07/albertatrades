from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)  
    search_query = models.CharField(default="", max_length=200)  
    search_location = models.CharField(default="", max_length=200)  
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Trade(models.Model):
    name = models.CharField(default="", max_length=200)
    query = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_counts = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % (self.name)

class UserSearchHistory(models.Model):
    user = models.ForeignKey(User)  
    query = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def date_time(self):
        return self.modified

