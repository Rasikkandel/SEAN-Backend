from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self , serializer) : 
        serializer.save(author=self.request.user) 

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all() 
    serializer_class = BlogSerializer