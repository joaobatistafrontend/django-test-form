from django.test import TestCase




from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from xhtml2pdf import pisa 
from django.views.generic import TemplateView

from .form import ContatoForm

#from .models import DadosFormModels



def contato(request):
     if str(request.method) == 'POST':
          form = ContatoForm(request.POST)
          if form.is_valid():
               form.send_email()
               form = ContatoForm()
     else:
          form = ContatoForm()
     context = {
          'form' : form
     }
     return render(request, 'form.html', context)