from django.db import models
from customer.models import Customer
from product.models import Product
from django.utils import timezone
# Create your models here.


class OrderStatus:
    IN_BASKET = 0
    PAYED = 1


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            self.created_at = timezone.now()
        super().save(force_insert, force_update, using, update_fields)
