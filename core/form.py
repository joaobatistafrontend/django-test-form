from django import forms
from .models import DadosFormModels

class DadosForm(forms.ModelForm):
     class meta:
          model = DadosFormModels
          filter = ['nome', 'email', 'subject', 'msg']

          