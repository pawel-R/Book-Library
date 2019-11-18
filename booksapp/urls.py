from django.urls import path
from . import views

app_name = "booksapp"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("results", views.search, name="search"),
    path("book_add", views.book_add, name="book_add"),
    path("book_import", views.book_import, name="book_import"),
    path("book/<int:pk>", views.book_detail, name="book_detail"),
]