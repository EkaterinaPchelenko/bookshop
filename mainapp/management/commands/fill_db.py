import json
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product, Author, ProductImage, Adds

import json, os

from users.models import User

JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    super_user = User.objects.create_superuser('Kate', 'user@bookshop.local', 'bookshop')

    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/categories.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        authors = load_from_json('mainapp/fixtures/authors.json')

        Author.objects.all().delete()
        for author in authors:
            auth = author.get('fields')
            auth['id'] = author.get('pk')
            new_author = Author(**auth)
            new_author.save()

        adds = load_from_json('mainapp/fixtures/adds.json')

        Adds.objects.all().delete()
        for add in adds:
            ad = add.get('fields')
            ad['id'] = add.get('pk')
            new_add = Adds(**auth)
            new_add.save()

        products = load_from_json('mainapp/fixtures/products.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            author = prod.get('author')
            _author = Author.objects.get(id=author)
            prod['author'] = _author
            category = prod.get('category')
            _category = ProductCategory.objects.get(id=category)
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()

        images = load_from_json('mainapp/fixtures/product_images.json')

        ProductImage.objects.all().delete()
        for image in images:
            im = image.get('fields')
            product = im.get('product')
            _product = Product.objects.get(id=product)
            im['product'] = _product
            new_image = ProductImage(**im)
            new_image.save()
