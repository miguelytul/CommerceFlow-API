from django.urls import path, include
from django.contrib import admin
from .views import ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='ProductListView'),
    
]