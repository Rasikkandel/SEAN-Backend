from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    choice = {
        'Frontend_development' : 'FRONTEND DEVLOPMENT' , 
        'Backend_development' : 'BACKEND DEVLOPMENT' , 
        'App_development' : 'APP DEVELOPMENT' , 
        'AI/ML' : 'AI/ML' , 
    }   
    sem = models.PositiveIntegerField(null=True, blank=True)          
    interested_stack = models.CharField(max_length=20 , blank=True , choices = choice) 
    
    def __str__(self):
        return self.username 


