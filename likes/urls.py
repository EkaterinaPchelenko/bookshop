from django.urls import path
from likes.views import like_action

app_name = 'likes'
urlpatterns = [
    path('like_action/<int:product_id>/', like_action, name='like_action'),
]
