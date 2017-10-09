# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cadastro
from django.contrib import admin


# Register your models here.
class CadastroAdmin(admin.ModelAdmin):
    model = Cadastro
    list_display = ['name', 'telefone']


admin.site.register(Cadastro, CadastroAdmin)
