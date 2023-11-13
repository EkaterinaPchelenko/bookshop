from django.urls import path

import users
from users.views import profile, login, logout, register

app_name = 'users'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
