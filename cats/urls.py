from django.urls import path

from . import views

app_name = "cats"

urlpatterns = [
    path("", views.index, name="index"),
]