# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cadastro
from django.shortcuts import render

# Create your views here.

def cadastro_list(request):
    cadastro = Cadastro.objects.all()
    context = {
        'cadastro_list': cadastro
    }

    return render(request, 'cadastro/template/lista.html', context)
