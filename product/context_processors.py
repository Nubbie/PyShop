from __future__ import absolute_import
from product.models import Category

__author__ = 'Elfix'


def categories(request):

    cats = Category.objects.all()
    added = {
        "categories": cats
    }
    return added
