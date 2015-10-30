from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.utils import timezone
# Create your models here.


class Customer(User):
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
    pass

