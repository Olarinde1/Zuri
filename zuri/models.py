from django.db import models


class Bookstore(models.Model):
    class Meta:
        verbose_name = "Book Store"
        verbose_name_plural = "Book Store"
    book_title = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)
    year_published = models.CharField(max_length=4)