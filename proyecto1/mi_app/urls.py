from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert_data, name='insert_data'),
    path('search/', views.search, name='search'),
]
