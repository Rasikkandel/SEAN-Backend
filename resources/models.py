from django.db import models
from django.conf import settings 

class Resource(models.Model):
    title = models.CharField(max_length=200)               
    description = models.CharField(max_length=500, blank=True)  
    file = models.FileField(upload_to='resources/', blank=True, null=True)  
    link = models.URLField(blank=True, null=True)         
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL, null=True, blank=True)  # user delete vayeni resource hudaina    
    is_active = models.BooleanField(default=True)         

    def __str__(self):
        return self.title
