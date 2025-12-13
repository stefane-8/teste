from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirecionamento profissional por tipo
            if user.tipo_usuario == 'diretoria':
                return redirect('admin_dashboard')

            elif user.tipo_usuario == 'associado':
                return redirect('minha_empresa')

            elif user.tipo_usuario == 'afiliado':
                return redirect('meu_perfil')

            return redirect('home')

        messages.error(request, "Usuário ou senha inválidos.")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso. Faça login.")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

@login_required
def meu_perfil(request):
    return render(request, 'accounts/perfil.html')
