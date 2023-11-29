from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, FormView

from baskets.models import Basket
from bookshop.mixin import BaseClassContextMixin
from likes.models import Like
from orders.models import Order, OrderItem
from users.forms import UserRegisterForm, UserLoginForm, UserProfileForm
from users.models import User


class RegisterListView(FormView, BaseClassContextMixin):

    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    title = 'BookWorld - Регистрация'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Подравляем! Вы успешно прошли регистрацию!')
            return redirect(self.success_url)
        return redirect(self.success_url)


class LoginListView(LoginView, BaseClassContextMixin):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'BookWorld - Авторизация'


class ProfileFormView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'BookWorld - Профиль'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileFormView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        context['likes'] = Like.objects.filter(user=self.request.user)
        context['orders'] = Order.objects.filter(user=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return redirect(self.success_url)


class Logout(LogoutView):
    template_name = 'mainapp/index.html'
