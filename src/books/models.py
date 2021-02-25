from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField("Название", max_length=80)
    # book_cover_photo = models.FileField("Обложка", upload_to=None, max_length=100)
    price = models.SmallIntegerField("Цена, руб.", blank=True, null=True,)
    author = models.ManyToManyField("dictionaries.Author", verbose_name="Автор")
    series = models.ForeignKey("dictionaries.BookSeries", verbose_name="Серия", on_delete=models.PROTECT)
    genre = models.ManyToManyField("dictionaries.Genre", verbose_name="Жанр")
    published_date = models.DateField("Год издания", blank=True, null=True)
    page_numbers = models.SmallIntegerField("Количество страниц", blank=True, null=True)
    binding = models.CharField("Переплет", max_length=80, blank=True, null=True)
    book_format = models.CharField("Формат", max_length=80, blank=True, null=True)
    isbn_num = models.CharField("ISBN", max_length=80, blank=True, null=True)
    weight = models.SmallIntegerField("Вес, г.", blank=True, null=True)
    age_restriction = models.SmallIntegerField("Возрастные ограничения", blank=True, null=True)
    publisher = models.ForeignKey("dictionaries.Publisher", verbose_name="Издательство", related_name = "Книги", on_delete=models.PROTECT)
    available_number = models.SmallIntegerField("В наличии, шт.", blank=True, null=True)
    yes = "Да"
    no = "Нет"
    is_available = models.CharField("Доступнны для заказа", choices=[(yes, "Да"), (no, "Нет")], default=yes, max_length=80) 
    rate = models.SmallIntegerField("Рейтинг", blank=True, null=True)
    creation_date = models.DateField("Дата внесения в каталог", blank=True, null=True)
    last_modifyed = models.DateField("Дата последнего изменения", blank=True, null=True)

    def __str__(self):
        return self.name
from django.db import models

