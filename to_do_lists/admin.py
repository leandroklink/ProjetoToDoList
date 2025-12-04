from django.contrib import admin
from .models import Tarefa #para conseguir acessar uma model no admin, ela deve ser importada nesse arquivo

# Register your models here.

admin.site.register(Tarefa)
