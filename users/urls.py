from django.urls import path
from django.views.generic import TemplateView

import users
from users.views import LoginListView, RegisterListView, ProfileFormView, Logout, basket_order

app_name = 'users'
urlpatterns = [
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('basket_order/', basket_order, name='basket_order'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('login/', LoginListView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    path('verify/<str:email>/<str:activation_key>/', RegisterListView.verify, name='verify')

]
