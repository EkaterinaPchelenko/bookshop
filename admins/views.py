from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryEditForm, ProductEditForm, AuthorEditForm
from users.models import User
from mainapp.models import Product, ProductCategory, Author


def index(request):
    return render(request, 'admins/admin.html')

class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'
        return context

class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Регистрация'
        return context

class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-read.html'
    success_url = reverse_lazy('admins:admins_user')

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AuthorListView(ListView):
    model = Author
    template_name = 'admins/admin-authors-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Авторы'
        return context


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'admins/admin-authors-create.html'
    form_class = AuthorEditForm
    success_url = reverse_lazy('admins:admins_author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создание автора'
        return context


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'admins/admin-authors-update-delete.html'
    form_class = AuthorEditForm
    context_object_name = 'author'
    success_url = reverse_lazy('admins:admins_author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление автора'
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'admins/admin-authors-update-delete.html'
    success_url = reverse_lazy('admins:admins_author')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthorDeleteView, self).dispatch(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        Author.objects.filter(id=self.object.id).delete()

        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Категории'
        return context


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoryEditForm
    success_url = reverse_lazy('admins:admins_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создание категории'
        return context


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryEditForm
    context_object_name = 'category'
    success_url = reverse_lazy('admins:admins_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление категории'
        return context


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins:admins_category')

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        ProductCategory.objects.filter(id=self.object.id).delete()

        return HttpResponseRedirect(self.get_success_url())


class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Категории'
        return context


class ProductCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-products-create.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('admins:admins_product')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создание продукта'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductEditForm
    context_object_name = 'product'
    success_url = reverse_lazy('admins:admins_product')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление продукта'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admins_product')

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        Product.objects.filter(id=self.object.id).delete()

        return HttpResponseRedirect(self.get_success_url())