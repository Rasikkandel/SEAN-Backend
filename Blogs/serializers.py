from rest_framework import serializers 
from Blogs.models import Blog
class BlogSerializer(serializers.ModelSerializer) : 

    class Meta : 
        model = Blog 
        fields = ['title','description','body']