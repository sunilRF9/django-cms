from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customers/<str:pk_test>', views.customers, name="customers"),
    path('products/', views.products, name="products"),
    path('', views.dash, name="home"),
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('create_customers/', views.createCustomer, name="create_customer"),
    path('dumps/', views.getExcel, name="dumps"),
]
