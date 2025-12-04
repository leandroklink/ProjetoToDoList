from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa
# Create your views here.


def index(request): #esse request é a requisição do usuário

    if request.user.is_authenticated:
        tarefas_total = Tarefa.objects.filter(user = request.user)

        if tarefas_total is not None: #verificando de a tarefas total não é nulo

            tarefas_concluidas = []
            tarefas_nao_concluidas = []

            for tarefa in tarefas_total:
                if tarefa.concluido ==True:
                    tarefas_concluidas.append(tarefa)
                else:
                    tarefas_nao_concluidas.append(tarefa)
        else:
            tarefas_concluidas = None
            tarefas_nao_concluidas = None

        if request.method == 'POST':
            form = TarefaForm(request.POST)

            if form.is_valid():
                user = request.user
                tarefa = form.cleaned_data["tarefa"]
                concluido = False
                new_tarefa = Tarefa.objects.create(user=user, tarefa=tarefa, concluido=concluido)
                new_tarefa.save() #salvar no banco de dados
                return redirect('index')
            else:
                context = {
                'form': form, 
                'tarefas_concluidas':tarefas_concluidas, 
                "tarefas_nao_concluidas": tarefas_nao_concluidas
                   }
                return render(request, "to_do_lists/index.html", context)
            


        form = TarefaForm()
        context = {
                'form': form, 
                'tarefas_concluidas':tarefas_concluidas, 
                "tarefas_nao_concluidas": tarefas_nao_concluidas
                   }
        return render(request, "to_do_lists/index.html", context)

    else:
        return render(request, 'to_do_lists/index.html')
    

def concluir(request, id):
    if request.user.is_authenticated: 
        tarefas_total = Tarefa.objects.filter(user = request.user)

        if tarefas_total is not None: #verificando de a tarefas total não é nulo

            for tarefa in tarefas_total:
                if tarefa.id == id:
                    tarefa.concluido = True 
                    tarefa.save() #salvando no BD

        return redirect('index')
                
    else: 
        return redirect('index')

def excluir(request, id):
    if request.user.is_authenticated: 
        tarefas_total = Tarefa.objects.filter(user = request.user)

        if tarefas_total is not None: #verificando de a tarefas total não é nulo

            for tarefa in tarefas_total:
                if tarefa.id == id: 
                    tarefa.delete() #salvando no BD

        return redirect('index')
                
    else: 
        return redirect('index')