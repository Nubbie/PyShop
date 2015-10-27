from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, null=True, default=None)
    created_at = models.DateTimeField(null=True, default=None)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            self.created_at = timezone.now()
        super().save(force_insert, force_update, using, update_fields)


class Picture(models.Model):
    path = models.FileField()
    product = models.ForeignKey(Product)
