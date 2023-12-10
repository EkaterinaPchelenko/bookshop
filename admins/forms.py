from django import forms

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from mainapp.models import ProductCategory, Product, Author, Adds


class UserAdminRegisterForm(UserRegisterForm):

    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image', 'address',
                  'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'


class UserAdminProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class AddEditForm(forms.ModelForm):
    class Meta:
        model = Adds
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ProductEditForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    class Meta:
        model = Product
        fields = ('name', 'author', 'image', 'description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name =='image' or field_name == 'category' or field_name == 'author':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
            # field.help_text = ''