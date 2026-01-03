from django.urls import path 
from .views import ResourceList , ResourceDetail


urlpatterns = [
path('<int:pk>/', ResourceDetail.as_view()),
path('', ResourceList .as_view()),
] 