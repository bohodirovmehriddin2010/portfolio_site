from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('', views.portfolio, name='portfolio'),
    path('', views.Blog, name='blog'),
]
