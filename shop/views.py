from django.views.generic import TemplateView, View
from product.models import Product
from customer.models import Customer
from shop.models import Order, OrderStatus
from django.contrib import messages
from django import http
from django.core.urlresolvers import reverse


class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        self.kwargs.update(kwargs)
        self.kwargs['last_product'] = Product.objects.all()

        return self.kwargs


class AddToBasket(View):
    def post(self, request):
        q = request.POST.get('quantity', 1)
        p = request.POST.get('product')
        back_url = request.META['HTTP_REFERER']
        product = Product.objects.filter(pk=p).first()
        customer = Customer.objects.filter(pk=request.user.id).first()
        if product is None:
            messages.error(request, "کالای مورد نظر وجود ندارد")
        elif customer is None:
            messages.error(request, "شما باید ابتدا لاگین کنید")
            return http.HttpResponseRedirect(reverse("customer:login"))
        else:
            new_order = Order.objects.filter(product=product).first() or Order()
            if new_order.pk is None:
                messages.success(request, "سفارش شما به سبد خرید افزوده شد")
            else:
                messages.success(request, "سفارش شما به روز گردید")

            new_order.customer = customer
            new_order.product = product
            new_order.quantity = q
            new_order.status = OrderStatus.IN_BASKET
            new_order.save()

        return http.HttpResponseRedirect(back_url)

    pass


class RemoveFromBasket(View):
    def get(self, request, **kwargs):
        order_id = kwargs.get('pk')
        customer = Customer.objects.filter(pk=self.request.user.id).first()
        if customer is None:
            messages.error(self.request, "شما باید ابتدا لاگین کنید")
            return http.HttpResponseRedirect(reverse("customer:login"))
        order = Order.objects.filter(customer=customer, pk=order_id).first()
        if order is not None:
            order.delete()
            messages.success(request, "سفارش مورد نظر حذف گردید")
        else:
            messages.warning(request, "امکان حذف سفارش وجود ندارد")
        return http.HttpResponseRedirect(reverse("shop:basket"))


class Checkout(TemplateView):
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        self.kwargs.update(kwargs)
        customer = Customer.objects.filter(pk=self.request.user.id).first()
        if customer is None:
            messages.error(self.request, "شما باید ابتدا لاگین کنید")
            return http.HttpResponseRedirect(reverse("customer:login"))
        orders = Order.objects.filter(status=OrderStatus.IN_BASKET, customer=customer).all()
        total_price = 0
        for o in orders:
            o.total = o.product.price * o.quantity
            total_price += o.total
        self.kwargs['orders'] = orders
        self.kwargs['total_price'] = total_price
        return self.kwargs


class GotoBank(TemplateView):
    template_name = 'gotobank.html'

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class BackFromBank(View):
    def get(self, request):
        result = request.GET.get('mode', 'danger').lower()
        customer = Customer.objects.filter(pk=self.request.user.id).first()
        if customer is None:
            messages.error(self.request, "شما باید ابتدا لاگین کنید")
            return http.HttpResponseRedirect(reverse("customer:login"))

        if result == "success":
            Order.objects.filter(customer=customer, status=OrderStatus.IN_BASKET).update(status=OrderStatus.PAYED)
            messages.success(request, "پرداخت با موفقیت انجام گردید")
        else:
            messages.error(request, "پرداخت ناموفق بود")
        return http.HttpResponseRedirect(reverse("shop:basket"))
