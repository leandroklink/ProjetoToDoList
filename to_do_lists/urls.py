from django.urls import path
from .views import (
    index,
    concluir,
    excluir,
    TarefaListCreateAPIView
)

urlpatterns = [
    path('', index, name='index'),
    path('concluir/<int:id>/', concluir, name='concluir'),
    path('excluir/<int:id>/', excluir, name='excluir'),

    # API
    path('api/tarefas/', TarefaListCreateAPIView.as_view(), name='api-tarefas'),
]
