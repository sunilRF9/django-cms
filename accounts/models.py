#coutinhod3dx9
from django.db import models
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=254,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "Name: {}, Email: {} and Phone: {}".format(self.name,self.email,self.phone)
