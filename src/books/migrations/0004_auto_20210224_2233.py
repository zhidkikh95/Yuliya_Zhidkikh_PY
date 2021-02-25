# Generated by Django 3.1.6 on 2021-02-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0002_auto_20210222_2210'),
        ('books', '0003_auto_20210224_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='dictionaries.Author', verbose_name='Автор'),
        ),
    ]
