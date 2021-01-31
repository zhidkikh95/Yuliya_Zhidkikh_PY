import datetime
from django.db import models

# Create your models here.
class Author(models.Model):
    surname = models.CharField("Фамилия", max_length=80)
    name = models.CharField("Имя", max_length=80)
    patronymic = models.CharField("Отчество", blank=True, null=True, max_length=80)
    country = models.CharField("Страна", blank=True, null=True, max_length=80)
    biography = models.TextField("Биография", blank=True, null=True)
    birthdate = models.DateField("Дата рождения", default=datetime.date(1970,1,1),  blank=True, null=True)

    def __str__(self):
        return self.surname

class Genre(models.Model):
    genre_name = models.CharField("Жанр", max_length=80)

    def __str__(self):
        return self.genre_name

class Publisher(models.Model):
    publisher_name = models.CharField("Издательство", max_length=80)
    publisher_description = models.TextField("Описание")

    def __str__(self):
     return self.publisher_name

class BookSeries(models.Model):
    series_name = models.CharField("Серия", max_length=80)

    def __str__(self):
        return self.series_name