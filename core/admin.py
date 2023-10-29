from django.contrib import admin
from .models import DadosFormModels

@admin.register(DadosFormModels)
class DadosADM(admin.ModelAdmin):
    list_display = ['nome', 'email', 'subject', 'msg']