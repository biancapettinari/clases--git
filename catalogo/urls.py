
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('editorial/', views.crear_editorial, name='crear_editorial'),
    path('libro/', views.crear_libro, name='crear_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]
