# Generated by Django 3.1.6 on 2021-02-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]