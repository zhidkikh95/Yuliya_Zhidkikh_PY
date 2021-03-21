from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name = "profile", on_delete=models.CASCADE)
    telephone = models.CharField("Номер телефона", max_length=100)
    address = models.TextField("Адрес")
    


