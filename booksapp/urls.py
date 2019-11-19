from django.urls import path, include
from . import views


app_name = "booksapp"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("results/", views.search, name="search"),
    path("book_add/", views.book_add, name="book_add"),
    path("book_import/", views.book_import, name="book_import"),
    path("book/<int:pk>", views.book_detail, name="book_detail"),
    path("book/<int:pk>/update", views.book_update, name="book_update"),
    path("book/<int:pk>/delete", views.book_delete, name="book_delete"),
    path("rest/", include("booksapp.api.urls")),

]