from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_en/', views.index_en, name='index_en'),
]
