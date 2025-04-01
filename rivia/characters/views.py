from django.views.generic import CreateView
from characters import models, forms 
from django.shortcuts import render

# Create your views here.
class char_creation(CreateView):
    model = models.Character
    template_name = 'char_creator.html'