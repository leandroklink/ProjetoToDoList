from django.db import models
from django.contrib.auth.models import User #modelo padrao de usuários do django

# Create your models here.
class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #o metodo CASCADE funciona de forma a deletar as tarefas também se o usuário for excluído
    tarefa = models.CharField(max_length=100)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.tarefa #com essa funcao quando olhar no painel adm, a tarefa vai aparecer na listagem como o nome dela