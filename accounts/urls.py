from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customers),
    path('products/', views.products),
    path('', views.dash),
]
