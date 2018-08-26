from django.urls import path,re_path 

from . import views

urlpatterns = [
    path('category/<slug:category_name_slug>/', views.category, name='category'),  
    path('', views.index, name='index'),
]
