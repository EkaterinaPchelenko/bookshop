from django.urls import path

from baskets.views import basket_add, basket_remove, basket_edit, basket_remove_from_products

app_name = 'baskets'
urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket'),
    path('remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('remove_from_products/<int:product_id>/', basket_remove_from_products, name='basket_remove_from_products'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]
