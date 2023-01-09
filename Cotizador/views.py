from django.shortcuts import render, get_object_or_404
from Cotizador.models import Neumatico
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

class NeumaticoDetalle(DetailView):
    model = Neumatico

class NeumaticoList(ListView):
    model = Neumatico

class NeumaticoCrear(CreateView):
  model = Neumatico
  success_url = "/panel-neumatico"
  fields = ["medida", "marca", "modelo"]

class NeumaticoBorrar(DeleteView):
  model = Neumatico
  success_url = "/panel-neumatico"

class NeumaticoActualizar(UpdateView):
  model = Neumatico
  success_url = "/panel-neumatico"
  fields = ["medida", "marca", "modelo"]