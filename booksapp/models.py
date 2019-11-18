from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publishedDate = models.CharField(max_length=15)
    type10 = models.CharField(max_length=10)
    identifier10 = models.CharField(max_length=20)
    type13 = models.CharField(max_length=10)
    identifier13 = models.CharField(max_length=20)
    pageCount = models.CharField(max_length=10, blank=True, null=True)
    smallThumbnail = models.URLField(max_length=200)
    thumbnail = models.URLField(max_length=200)
    language = models.CharField(max_length=10)

    def __str__(self):
        return self.title