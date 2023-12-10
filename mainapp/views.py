from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.views.decorators.cache import cache_page, never_cache

from django.conf import settings

from baskets.models import Basket
from likes.models import Like
from mainapp.models import Product, ProductCategory, ProductImage, Adds


def index(request):
    return render(request, 'mainapp/index.html')


@never_cache
def products(request, category_id=None, page_id=1):
    product_in_basket = []
    product_liked = []
    products = Product.objects.filter(category_id=category_id).select_related(
        'category') if category_id != None else Product.objects.all()

    paginator = Paginator(products, per_page=6)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    for product in Product.objects.all():
        for basket in Basket.objects.all():
            if product.id == basket.product_id:
                product_in_basket.append(product.id)
        for like in Like.objects.all():
            if product.id == like.product_id:
                product_liked.append(product.id)

    adds = Adds.objects.all()
    context = {
        "title": "BookWorld",
        "products": products_paginator,
        "categories": ProductCategory.objects.all(),
        "product_in_basket": product_in_basket,
        "product_liked": product_liked,
        "adds": adds,
    }
    context['first_add'] = context['adds'][0]
    context['len_add'] = len(context['adds'])
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user)
        context["baskets"] = baskets

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
        product_liked = []
        product_in_basket = []
        context = super().get_context_data()
        for product in Product.objects.all():
            for like in Like.objects.all():
                if product.id == like.product_id:
                    product_liked.append(product.id)
            for basket in Basket.objects.all():
                if product.id == basket.product_id:
                    product_in_basket.append(product.id)

        context['product'] = get_product(self.kwargs.get('pk'))
        context['images'] = ProductImage.objects.filter(product_id=context['product'].id)
        context['categories'] = ProductCategory.objects.all()
        context['im_len'] = len(context['images'])
        # context['first_im'] = context['images'][0]
        context['product_liked'] = product_liked
        context['product_in_basket'] = product_in_basket
        return context
# Create your views here.
