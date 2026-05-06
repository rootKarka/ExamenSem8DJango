from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_restaurantes, name='lista'),
    path('crear/', views.crear_restaurante, name='crear'),
    path('editar/<int:id>/', views.editar_restaurante, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_restaurante, name='eliminar'),
]