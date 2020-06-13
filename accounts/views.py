from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def customers(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request,'accounts/customers.html',context)

def dash(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_cus = customers.count()
    total_ord = orders.count()
    deliver = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders,'customers':customers,
            'total_ord':total_ord, 'deliver':deliver, 'pending':pending
            }
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'products':products})
