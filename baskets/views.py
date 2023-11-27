from django.http import JsonResponse

from django.shortcuts import HttpResponseRedirect, render
from django.template.loader import render_to_string

from mainapp.models import Product
from baskets.models import Basket

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def basket_add(request, product_id):
    user_select = request.user
    product = Product.objects.get(id=product_id)
    Basket.objects.create(user=user_select, product=product, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, basket_id):
    Basket.objects.get(id=basket_id).delete()
    baskets = Basket.objects.filter(user=request.user)
    context = {
        'baskets': baskets
    }
    result = render_to_string('baskets/basket.html', context)
    return JsonResponse({'result': result})


@login_required
def basket_remove_from_products(request, product_id):
    product = Product.objects.get(id=product_id)
    print(Basket.objects.get(product=product))
    Basket.objects.get(product=product).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required()
def basket_edit(request, id, quantity):
    if is_ajax(request=request):
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)
        context = {
            'baskets': baskets
        }
        result = render_to_string('baskets/basket.html', context)
        return JsonResponse({'result': result})


def basket_quantity(request):

    baskets = Basket.objects.filter(user=request.user)
    context = {
        "baskets": baskets,
    }
    return render(request, 'basket/basket_quantity.html', context)