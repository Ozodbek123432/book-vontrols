from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField()
    pice = models.CharField(max_length=30, default='0 som')
    have = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name