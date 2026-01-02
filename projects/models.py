from django.db import models
from django.conf import settings
# Create your models here.
class Project(models.Model) : 
    Author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL ,null=True , blank=True) # user delete vayeni project chai hudaina 
    title = models.CharField(max_length=200) 
    description = models.CharField(max_length=500 , blank=True)
    details = models.TextField(blank = True) 
    posted_at = models.DateTimeField(auto_now_add = True) 
    updated_at = models.DateTimeField(auto_now = True) 
    github_url = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='project_thumbnails/', blank=True, null=True) 

    def __str__(self):
        return self.title 
