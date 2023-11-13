from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11}$',
                                 message="Номер телефона должен соответствовать формату '+79999999999' и содержать 11 знаков")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)
    address = models.CharField(blank=True, max_length=256)