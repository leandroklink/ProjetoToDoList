from django.shortcuts import render, redirect
from .forms import MyPassworChangeForm, MyUserCreationForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if  request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sucesso')
        else:
            context = {'form':form}
            return render(request, 'register/register.html', context)


    form = MyUserCreationForm()
    context = {'form':form}
    return render(request, 'register/register.html', context)
    


def reset_pass(request):
    if request.user.is_authenticated:

        if request.method =='POST':
            form = MyPassworChangeForm(user=request.user, data=request.POST)

            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('reset_sucesso')
            
            else:
                context = {'form': form }
                return render(request, 'register/reset_pass.html', context)

        form = MyPassworChangeForm(user=request.user)
        context = {'form':form}

        return render(request, 'register/reset_pass.html', context)
    else:
        return redirect('index')

def sucesso(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'register/sucesso.html')

def reset_sucesso(request):
    if request.user.is_authenticated:
        return render(request, 'register/reset_sucesso.html')
    return redirect('index')