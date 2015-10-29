from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product.models import Product, Category


class ProductList(ListView):
    template_name = 'list.html'
    category = None

    def get_category(self):
        if self.category is None:
            self.category = Category.objects.filter(pk=self.request.GET.get('cat', None)).first()
        return self.category

    def get_queryset(self):
        if self.get_category() is not None:
            return Product.objects.filter(category=self.get_category()).all()
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['category']=self.get_category()
        return context


class ProductDetails(DetailView):
    template_name = 'details.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            return Product.objects.filter(pk=pk).first()
        return None
