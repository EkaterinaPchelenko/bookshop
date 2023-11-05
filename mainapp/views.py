from django.shortcuts import render

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

# Create your views here.
