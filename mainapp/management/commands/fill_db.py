import json
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product, Author
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
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
