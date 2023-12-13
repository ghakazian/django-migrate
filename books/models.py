from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True)
    publisher = models.ForeignKey('books.Publisher', on_delete=models.CASCADE, null=True)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
