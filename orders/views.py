from django.views.generic import ListView

from orders.models import Order


class OrderList(ListView):
    model = Order
    fields = []

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)
