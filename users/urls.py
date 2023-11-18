from django.urls import path

import users
from users.views import LoginListView, RegisterListView, ProfileFormView, Logout

app_name = 'users'
urlpatterns = [
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('login/', LoginListView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
