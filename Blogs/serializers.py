from rest_framework import serializers 
from Blogs.models import Blog
class BlogSerializer(serializers.ModelSerializer) : 
    author = serializers.ReadOnlyField(source="author.username")
    class Meta : 
        model = Blog 
        fields = ['title','description','body','author']