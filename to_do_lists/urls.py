
from django.urls import path
from . import views # o . serve pra mostrar ao django que é pra importar da própria pasta onde está o arquivo (da minha própria pasta, importe... )

urlpatterns = [
    path('', views.index, name='index'), #arquivo views, função index, e com a rota com nome de index aqui
    path('concluir/<int:id>', views.concluir, name='concluir'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
]
