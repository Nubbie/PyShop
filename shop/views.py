from django.views.generic import TemplateView
from product.models import Product


class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        self.kwargs.update(kwargs)
        self.kwargs['last_product'] = Product.objects.all()

        return self.kwargs
