from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(verbose_name="Название", max_length=80)
    book_picture = models.ImageField(verbose_name="Обложка", upload_to='uploads/')
    price = models.DecimalField(verbose_name="Цена, руб.", max_digits=5, decimal_places=2, blank=True, null=True)
    author = models.ManyToManyField("dictionaries.Author", verbose_name="Автор")
    series = models.ForeignKey("dictionaries.BookSeries", verbose_name="Серия", on_delete=models.PROTECT)
    genre = models.ManyToManyField("dictionaries.Genre", verbose_name="Жанр")
    published_year = models.PositiveSmallIntegerField(verbose_name="Год издания", blank=True, null=True)
    page_numbers = models.PositiveSmallIntegerField("Количество страниц", blank=True, null=True)
    binding = models.CharField(verbose_name="Переплет", max_length=80, blank=True, null=True)
    book_format = models.CharField(verbose_name="Формат", max_length=80, blank=True, null=True)
    isbn_num = models.CharField(verbose_name="ISBN", max_length=80, blank=True, null=True)
    weight = models.PositiveSmallIntegerField(verbose_name="Вес, г.", blank=True, null=True)
    age_restriction = models.PositiveSmallIntegerField(verbose_name="Возрастные ограничения", blank=True, null=True)
    publisher = models.ForeignKey("dictionaries.Publisher", verbose_name="Издательство", related_name = "Книги", on_delete=models.PROTECT)
    available_number = models.PositiveIntegerField(verbose_name="В наличии, шт.", blank=True, null=True)
    yes = "Да"
    no = "Нет"
    is_available = models.CharField(verbose_name="Доступнны для заказа", choices=[(yes, "Да"), (no, "Нет")], default=yes, max_length=80) 
    rate = models.PositiveSmallIntegerField(verbose_name="Рейтинг", blank=True, null=True)
    created = models.DateTimeField(verbose_name="Дата внесения в каталог", auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(verbose_name="Дата последнего изменения", auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

