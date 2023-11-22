from django.urls import path

from .views import OrderList

from mainapp.views import index

app_name = 'orders'
urlpatterns = [
    path('', OrderList.as_view(), name='list'),
]