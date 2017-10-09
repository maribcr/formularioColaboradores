from django import forms
from .models import *
import requests
from .models import Cadastro


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
