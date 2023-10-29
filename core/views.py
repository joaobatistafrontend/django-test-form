from django.shortcuts import render, redirect
from django.views.generic import TemplateView,CreateView
from .form import DadosForm
from .models import DadosFormModels
from django.urls import reverse_lazy

def index(request):
     if request.method == 'POST':
          form = DadosForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('index')
          
     else:
          form = DadosForm
     return render(request, 'form.html', {'from':form})