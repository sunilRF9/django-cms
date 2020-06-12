from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def customers(request):
    return render(request,'accounts/customers.html')
def dash(request):
    return render(request,'accounts/dashboard.html')
def products(request):
    return render(request,'accounts/products.html')
