from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa

# 🔹 IMPORTS DO DRF (FORA DAS FUNÇÕES)
from rest_framework import generics, permissions
from .serializers import TarefaSerializer


# ======================
# VIEWS HTML (JÁ EXISTENTES)
# ======================

def index(request):

    if request.user.is_authenticated:
        tarefas_total = Tarefa.objects.filter(user=request.user)

        tarefas_concluidas = []
        tarefas_nao_concluidas = []

        for tarefa in tarefas_total:
            if tarefa.concluido:
                tarefas_concluidas.append(tarefa)
            else:
                tarefas_nao_concluidas.append(tarefa)

        if request.method == 'POST':
            form = TarefaForm(request.POST)

            if form.is_valid():
                Tarefa.objects.create(
                    user=request.user,
                    tarefa=form.cleaned_data["tarefa"],
                    concluido=False
                )
                return redirect('index')

        form = TarefaForm()
        context = {
            'form': form,
            'tarefas_concluidas': tarefas_concluidas,
            'tarefas_nao_concluidas': tarefas_nao_concluidas
        }
        return render(request, "to_do_lists/index.html", context)

    return render(request, 'to_do_lists/index.html')


def concluir(request, id):
    if request.user.is_authenticated:
        Tarefa.objects.filter(
            id=id,
            user=request.user
        ).update(concluido=True)

    return redirect('index')


def excluir(request, id):
    if request.user.is_authenticated:
        Tarefa.objects.filter(
            id=id,
            user=request.user
        ).delete()

    return redirect('index')


# ======================
# API REST (NOVA)
# ======================

class TarefaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from django.shortcuts import render

def reset_pass(request):
    return render(request, 'to_do_lists/reset_pass.html')
