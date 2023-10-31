from django.urls import path
from .views import contato,i
urlpatterns = [
    path('', contato, name='contato'),
]