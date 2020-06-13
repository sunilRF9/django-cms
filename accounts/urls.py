from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customers/<str:pk_test>', views.customers, name="customers"),
    path('products/', views.products, name="products"),
    path('', views.dash, name="home"),
]
