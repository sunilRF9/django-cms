from django.db import models
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=254,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "Name: {}, Email: {} and Phone: {}".format(self.name,self.email,self.phone)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY= (
            ('Indoor','Indoor'),
            ('Outdoor', 'Outdoor'),
            )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return "Name: {} and Price: {}".format(self.name,self.price)

class Order(models.Model):
    STATUS = (
            ('Pending','Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
            )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True) 
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    def __str__(self):
        return "Status: {}".format(self.status)