from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lugares", views.S2ndView, name="S2ndView"),
    path("test", views.ShowData, name="ShowData")
]