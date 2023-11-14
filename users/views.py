from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.forms import UserRegisterForm, UserLoginForm, UserProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Подравляем! Вы успешно прошли регистрацию!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'BookWorld - Регистрция',
        'form': form
    }
    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()
    context = {
        'title': 'BookWorld - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль сохранён.')
        else:
            messages.error(request, 'Профиль не сохранён!')
        return HttpResponseRedirect(reverse('users:profile'))

    context = {
        'title': 'Профиль',
        'form': UserProfileForm(instance=request.user),
        # 'baskets': Basket.objects.filter(user=request.user),

    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
