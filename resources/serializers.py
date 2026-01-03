from rest_framework import serializers 
from resources.models import Resource
class ResourceSerializer(serializers.ModelSerializer) : 
    author = serializers.ReadOnlyField(source="author.username")
    class Meta : 
        model = Resource
        fields = ['id','title','description','file','author','created_at', 'updated_at']  


 
