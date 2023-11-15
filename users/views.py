from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from users.forms import UserRegisterForm, UserLoginForm, UserProfileForm
from users.models import User


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


class ProfileFormView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'GeekShop - Профиль'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileFormView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            print(form)
        return redirect(self.success_url)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
