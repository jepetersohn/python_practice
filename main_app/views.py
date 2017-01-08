# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
  # return HttpResponse('<h1>Hello Explorers!</h1>')
  # name = 'Gold Nugget'
  # value = 1000.00
  # context = {'treasure_name' : name,
  #             'treasure_val' : value}
  return render(request, 'index.html', {'aliens' : aliens})

class Alien:
  def __init__(self, name, diet, home_planet):
    self.name = name
    self.diet = diet
    self.home_planet = home_planet

aliens = [
  Alien("Alf", 'cats', "Melmac"),
  Alien('E.T.', 'M&Ms', "Brodo Asogi"),
  Alien('Kal-El ', 'powered by sun; does not need to eat', 'Krypton'),
  ]