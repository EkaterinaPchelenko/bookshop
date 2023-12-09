from django.urls import path
from .views import (index, UserCreateView, UserUpdateView, UserDeleteView, UserListView, CategoryListView,
                    CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
                    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, AuthorListView,
                    AuthorCreateView, AuthorUpdateView, AuthorDeleteView)

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_user'),
    path('users-create/', UserCreateView.as_view(), name='admins_user_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admins_user_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admins_user_delete'),

    path('authors/', AuthorListView.as_view(), name='admins_author'),
    path('authors-create/', AuthorCreateView.as_view(), name='admins_author_create'),
    path('authors-update/<int:pk>/', AuthorUpdateView.as_view(), name='admins_author_update'),
    path('authors-delete/<int:pk>/', AuthorDeleteView.as_view(), name='admins_author_delete'),

    path('categories/', CategoryListView.as_view(), name='admins_category'),
    path('categories-create/', CategoryCreateView.as_view(), name='admins_category_create'),
    path('categories-update/<int:pk>/', CategoryUpdateView.as_view(), name='admins_category_update'),
    path('categories-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admins_category_delete'),

    path('products/', ProductListView.as_view(), name='admins_product'),
    path('products-create/', ProductCreateView.as_view(), name='admins_product_create'),
    path('products-update/<int:pk>/', ProductUpdateView.as_view(), name='admins_product_update'),
    path('products-delete/<int:pk>/', ProductDeleteView.as_view(), name='admins_product_delete'),

]
