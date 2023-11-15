from django.urls import path

import users
from users.views import login, logout, register, ProfileFormView

app_name = 'users'
urlpatterns = [
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
