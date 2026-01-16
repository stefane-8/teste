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
                return redirect('associado_dashboard')

            elif user.tipo_usuario == 'afiliado':
                return redirect('meu_perfil')
            
            elif user.tipo_usuario == 'coletivo':
                return redirect('coletivo_dashboard')

            

            return redirect('home')

        messages.error(request, "Usuário ou senha inválidos.")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})

from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Mapeia tipo_usuario -> nome do Group
            mapa = {
                "diretoria": "Diretoria",
                "associado": "Associado",
                "afiliado": "Afiliado",
                "coletivo": "Coletivo/Institucional",
            }

            nome_grupo = mapa.get(user.tipo_usuario, "Afiliado")

            # Garante que o grupo exista 
            try:
                grupo = Group.objects.get(name=nome_grupo)
                user.groups.add(grupo)
            except Group.DoesNotExist:
                # Se o grupo não existir ainda, não quebra o cadastro
                pass

            messages.success(request, "Conta criada com sucesso. Faça login.")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

@login_required
def diretoria_dashboard(request):
    return render(request, 'diretoria/dashboard.html')

@login_required
def associado_dashboard(request):
    if request.user.tipo_usuario != 'associado':
        return redirect('home')
    return render(request, 'associado/dashboard.html')


@login_required
def meu_perfil(request):
    return render(request, 'accounts/perfil.html')

@login_required
def coletivo_dashboard(request):
    if request.user.tipo_usuario != 'coletivo':
        return redirect('home')
    return render(request, 'coletivo/dashboard.html')

