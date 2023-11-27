from django.urls import path

from .views import OrderList, read, order_forming_complete, create_order, view_order

from mainapp.views import index

app_name = 'orders'
urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    # path('read/<int:pk>/', OrderDetail.as_view(), name='read'),
    # path('detail/', read, name='read'),
    path('view/', view_order, name='view'),
    path('create/', create_order, name='create'),
    path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),
]