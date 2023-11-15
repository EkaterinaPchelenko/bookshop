
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Номер телефона должен соответствовать формату '+79999999999' и содержать 11 знаков", regex='^\\+?1?\\d{11}$')]),
        ),
    ]