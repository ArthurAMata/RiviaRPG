from django.shortcuts import render
from .models import Personagem

def lista_personagens(request):
    personagens = Personagem.objects.all()
    return render(request, 'personagens/lista_personagens.html', {'personagens': personagens})
