from django.urls import path
from . import views

urlpatterns = [
    path('personagens/', views.lista_personagens, name='lista_personagens'),
]