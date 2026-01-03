from rest_framework import generics
from .models import Resource
from .serializers import ResourceSerializer

class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def perform_create(self , serializer) : 
        serializer.save(author=self.request.user)


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer 
