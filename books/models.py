# coding=utf-8

from django.db import models

from main.settings import DATE_INPUT_FORMATS


class Book(models.Model):
    objects = None
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    def __str__(self):
        return self.name + " " + self.author
