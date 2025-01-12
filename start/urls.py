from django.urls import path

from . import views

app_name = "start"

urlpatterns = [
    path("", views.index, name="index"),
    path("haha/",views.index_haha, name="index_haha")
]