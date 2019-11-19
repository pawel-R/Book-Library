from django.urls import path, include
from . import views
from rest_framework import routers


app_name = "api"

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("book/<int:pk>/", views.api_detail, name="detail"),
    path("book/<int:pk>/update/", views.api_update, name="update"),
    path("book/<int:pk>/delete/", views.api_delete, name="delete"),
    path("book/create", views.api_create, name="create"),
    path("book/", views.ApiBookList.as_view(), name="list"),

]