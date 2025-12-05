# ToDoLists Django

Projeto de estudos em Django para implementar uma To-Do List (Registros de atividades) utilizando python e django.

Esse projeto foi feito com base no Curso de Django: To-Do-List de Jefferson Lobato no Youtube 
Segue link do curso:
https://youtube.com/playlist?list=PLLVddSbilcunGg0IJ4zP05Z91yrEaIiQh&si=KRHI1fdyTR4bqVnk

##  Tecnologias

- Python 
- Django 
- Outras libs –  `requirements.txt`

## Funcionalidades


- Criar, editar, remover tarefas
- Marcar tarefas como concluídas
- Autenticação de usuários (login / logout)
- Adicionei uma nova funcionalidade que permite excluír tarefas já concluídas, planejo continuar a atualizar esse projeto em breve com novas funcionalidades

##  Como rodar localmente

### Pré-requisitos

- Python instalado (versão compatível)  
- `venv` (ou outro ambiente virtual)

## Passos

###  1. Clone este repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

##  2. Crie um ambiente virtual
python -m venv venv

##  3. Ative o ambiente virtual
##  No Windows:
venv\Scripts\activate
##  No Linux / macOS:
source venv/bin/activate

##  4. Instale as dependências
pip install -r requirements.txt

##  5. Rode as migrações do banco de dados
python manage.py migrate

##  6. (Opcional) Crie um superusuário/admin
python manage.py createsuperuser

## 7. Inicie o servidor de desenvolvimento
python manage.py runserver


<img width="1384" height="618" alt="ToDoList" src="https://github.com/user-attachments/assets/377b080a-6f5e-464a-a1b6-4e34146d0df5" />
