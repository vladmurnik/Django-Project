from django.urls import path

from . import views

app_name = "prime_number"

urlpatterns = [
    path("", views.number, name="number"),
]