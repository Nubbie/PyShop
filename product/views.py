from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product.models import Product, Category


class ProductList(ListView):
    template_name = 'list.html'

    def get_queryset(self):
        category = self.request.GET.get('cat', None)
        if category is not None:
            category = Category.objects.filter(pk=category).first()
            return Product.objects.filter(category=category).all()
        return Product.objects.all()


class ProductDetails(DetailView):
    template_name = 'details.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            return Product.objects.filter(pk=pk).first()
        return None
