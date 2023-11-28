from django.urls import path

from . import views

urlpatterns = [
    path("home/index/", views.index, name="index"),
    path("home/index/lugares/<str:lugar>", views.S2ndView, name="S2ndView"),
    path("test", views.ShowData, name="ShowData"), 
    path('home/formulario/', views.mostrar_formulario, name='mostrar_formulario'),
    path('guardar_lugar/', views.guardar_lugar, name='guardar_lugar'),
    path('home/', views.home, name='inicio'),
    path('home/index/paginadeayuda.html', views.ayuda, name='ayuda'),

]