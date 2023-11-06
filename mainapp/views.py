from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.decorators.cache import cache_page, never_cache

from django.conf import settings
from mainapp.models import Product, ProductCategory


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        "title": "bookshop",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    return get_object_or_404(Product, pk=pk)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/product_item.html'
    context_object_name = 'product'

    def get_context_data(self, category_id=None, *args, **kwargs):
        context = super().get_context_data()

        context['product'] = get_product(self.kwargs.get('pk'))
        context['categories'] = ProductCategory.objects.all()
        return context
# Create your views here.
