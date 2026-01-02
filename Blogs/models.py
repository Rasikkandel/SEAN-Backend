from django.db import models
from django.conf import settings

class Blog(models.Model):
    name = models.CharField(max_length=200)  
    description = models.CharField(max_length=500) 
    body = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)      
    author = models.ForeignKey(settings.AUTH_USER_MODEL  , on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        return self.name

