from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username'] #estudar cleaned_data depois
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password) #validação de usuário

            if user is not None:         #se o usuário existe
                login(request, user)
                return redirect('index')


            else:
                form.add_error('username', 'Credenciais inválidas.')
                context = {'form': form}
                return render(request,'authenticated/login.html', context)
            
        else:
            context = {'form': form}
            return render(request, 'authenticated/login.html', context)



    form = LoginForm()
    context = {'form': form}
    return render(request,'authenticated/login.html', context)

@login_required(login_url="login_page")#se nao estiver logado vai para a tela de login
def logout_page(request):
    logout(request)
    return redirect('index')