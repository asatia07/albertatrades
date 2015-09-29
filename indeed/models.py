from django.db import models

# Create your models here.

class Trade(models.Model):
    name = models.CharField(default="", max_length=200)
    query = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_counts = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

