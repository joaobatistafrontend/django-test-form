from django.db import models

class DadosFormModels(models.Model):
     nome = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     subject = models.CharField(max_length=100)
     msg = models.TextField()