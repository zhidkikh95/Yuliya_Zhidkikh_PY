# Generated by Django 3.1.6 on 2021-03-09 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0002_auto_20210308_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='Корзина пользователя'),
        ),
    ]
