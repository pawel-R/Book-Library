from rest_framework import serializers
from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id",
                  "title",
                  "authors",
                  "publishedDate",
                  "type10",
                  "identifier10",
                  "type13",
                  "identifier13",
                  "pageCount",
                  "smallThumbnail",
                  "thumbnail",
                  "language")
