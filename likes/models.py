from django.db import models

from mainapp.models import Product
from users.models import User


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Понравившийся товар для {self.user.username} | Товар {self.product.name}'

