from django.urls import path
from .views import index, article, about

urlpatterns = [
    path("", index, name="index"),
    path("article/", article, name="article"),
    path("about/", about, name="about"),
]
