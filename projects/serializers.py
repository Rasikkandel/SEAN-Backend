from rest_framework import serializers 
from projects.models import Project
class ProjectSerializer(serializers.ModelSerializer) : 
    author = serializers.ReadOnlyField(source="author.username")
    class Meta : 
        model = Project
        fields = ['title','description','details', 'github_url','live_link','thumbnail'] 
