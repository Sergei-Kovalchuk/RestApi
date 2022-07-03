from django.db import models


class Create(models.Model):
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)




