from django.http import JsonResponse

from django.shortcuts import HttpResponseRedirect, render
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required

from likes.models import Like
from mainapp.models import Product


# Create your views here.


@login_required
def like_action(request, product_id):
    user_select = request.user
    product = Product.objects.get(id=product_id)
    likes = Like.objects.filter(user=user_select, product=product)
    if not likes.exists():
        Like.objects.create(user=user_select, product=product)
    else:
        like = likes.first()
        like.delete()
    context = {
        'likes': likes
    }
    result = render_to_string('mainapp/products.html')
    return JsonResponse({'result': result}, context)

# @login_required
# def basket_remove(request, basket_id):
#     Basket.objects.get(id=basket_id).delete()
#     baskets = Basket.objects.filter(user=request.user)
#     context = {
#         'baskets': baskets
#     }
#     result = render_to_string('baskets/basket.html', context)
#     return JsonResponse({'result': result})