from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        "title": "bookworld",
        "products": [
            {"url": "#",
             "name": "Роман1",
             "price": "1000 руб.",
             "description":  "Какой-то роман"},
            {"url": "#",
             "name": "Роман2",
             "price": "1000 руб.",
             "description": "Какой-то роман"},
            {"url": "#",
             "name": "Роман3",
             "price": "1000 руб.",
             "description": "Какой-то роман"},
            {"url": "#",
             "name": "Роман4",
             "price": "1000 руб.",
             "description": "Какой-то роман"},
            {"url": "#",
             "name": "Роман5",
             "price": "1000 руб.",
             "description": "Какой-то роман"},
            {"url": "#",
             "name": "Роман6",
             "price": "1000 руб.",
             "description": "Какой-то роман"},
            {"url": "#",
             "name": "Роман7",
             "price": "1000 руб.",
             "description": "Какой-то роман"},
        ]
    }
    return render(request, 'mainapp/products.html', context)

# Create your views here.
