from django.urls import path

from . import views

app_name = "haha"

urlpatterns = [
    path("hash/", views.cipher, name="index"),
    path("cipher/", views.cipher_adik, name="adik")
]