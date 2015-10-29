from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


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

    def __str__(self):
        return "{0}:{1}".format(self.name, self.description)


class Picture(models.Model):
    path = models.FileField()
    product = models.ForeignKey(Product)

    def __str__(self):
        return "image : {0}".format(self.path)
