from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CreateUserForm, CreateCustomerForm
from .filter import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Deleted User Regs and Login
def customers(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs

    context = {'customer':customer, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter}
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

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset = Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    formset = OrderForm(instance=order)
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        formset = OrderForm(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method ==  'POST':
        order.delete()
        return redirect('/')
    context = {'item':order} 
    return render(request, 'accounts/delete.html', context)
def createCustomer(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'accounts/createcustomer.html', context)
def getExcel(request):
    import csv
    import sqlite3
    import pandas
    con = sqlite3.connect('db.sqlite3')
    one = """
    SELECT accounts_customer.name, accounts_customer.phone, accounts_customer.email  FROM accounts_customer INNER JOIN accounts_order ON accounts_customer.id = accounts_order.customer_id;"""
    two = """
    SELECT accounts_product.pname, accounts_product.price, accounts_order.date_created FROM accounts_product  INNER JOIN accounts_order ON accounts_product.id = accounts_order.product_id;"""
    df = pandas.read_sql_query(one, con)
    df2 = pandas.read_sql_query(two, con)
    print(df2)
    dfn2 = df2.iloc[::-1]
    print(dfn2)
    final = pandas.concat([df, df2.iloc[::-1]], axis=1)
    print(final)
    from datetime import datetime
    # current date and time
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    print("timestamp =", timestamp)
    dt_object = datetime.fromtimestamp(timestamp)
    final.to_csv(r'dumps_' + str(dt_object) + '.csv',index = False, header=True)
    return HttpResponse('Saved Data')
