from django.shortcuts import render
from django.views.generic import ListView, DetailView

from bookshop.mixin import BaseClassContextMixin
from orders.models import Order


class OrderList(ListView):
    model = Order
    fields = []

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)


# class OrderDetail(DetailView, BaseClassContextMixin):
#     model = Order
#     title = 'BookWorld | Просмотр заказа'

def read(request):
    context = {
        'title': 'BookWorld | Просмотр заказа',

    }
    return render(request, 'orders/order_detail.html', context)