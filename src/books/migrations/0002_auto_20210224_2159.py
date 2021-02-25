# Generated by Django 3.1.6 on 2021-02-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=80, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Серия'),
        ),
    ]
