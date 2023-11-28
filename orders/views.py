from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from baskets.models import Basket
from bookshop.mixin import BaseClassContextMixin
from orders.models import Order, OrderItem


class OrderList(ListView):
    model = Order
    fields = []

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)


def view_order(request):
    def word_form(q):
        if q % 10 == 1:
            return 'товар'
        elif 1 < q % 10 < 5:
            return 'товара'
        elif 4 < q % 10 < 11:
            return 'товаров'
        else:
            word_form(q % 10)

    print(request)
    baskets = Basket.objects.filter(user=request.user)
    quantity = baskets[0].total_quantity()
    word = word_form(quantity)

    context = {
        'baskets': baskets,
        'title': 'BookWorld | Просмотр заказа',
        'word': word,
    }
    return render(request, 'orders/order_form.html', context)

def create_order(request):
    print(request.method)
    if request.method == 'POST':
        address = request.POST.get('address')
        print(request)
        # payment_method = request.POST.get('payment_method')

        order = Order.objects.create(user=request.user, address=address)
        order.status = Order.PROCEEDED

        baskets = Basket.objects.filter(user=request.user)

        for basket in baskets:
            if basket.product.quantity > 0:
                order_it = OrderItem.objects.create(order=order, product=basket.product, quantity=basket.quantity)
                order_it.save()

        order.status = Order.PAID
        order.save()
        baskets = Basket.objects.filter(user=request.user)
        for basket in baskets:
            basket.delete()

        return HttpResponseRedirect(reverse('users:profile'))


# class OrderDetail(DetailView, BaseClassContextMixin):
#     model = Order
#     title = 'BookWorld | Просмотр заказа'


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()

    return HttpResponseRedirect(reverse('orders:list'))

def read(request):
    pass