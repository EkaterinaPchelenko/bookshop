from django.urls import path
import mainapp.views as mainapp
from baskets.views import basket_quantity

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:category_id>/', mainapp.products, name='category'),
    path('detail/<int:pk>/', mainapp.ProductDetail.as_view(), name='detail'),
    path('page/<int:page_id>/', mainapp.products, name='page'),

]
