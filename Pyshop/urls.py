from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^account/', include('customer.urls', namespace="customer", app_name="customer")),
    url(r'^product/', include('product.urls', namespace="product", app_name="product")),
    url(r'', include('shop.urls',namespace="shot",app_name="shop"))
]
