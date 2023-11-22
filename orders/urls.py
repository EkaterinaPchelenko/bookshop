from django.urls import path

from .views import OrderList, read

from mainapp.views import index

app_name = 'orders'
urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    # path('read/<int:pk>/', OrderDetail.as_view(), name='read'),
    path('detail/', read, name='read'),
]