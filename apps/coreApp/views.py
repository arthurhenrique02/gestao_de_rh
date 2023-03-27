from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# definir view home
# necessario estar logado para acessar a rota
@login_required(login_url="/accounts/")
def home(request):  # request como argumento para poder pegar a requisição do usuário
    return render(request, "index.html")
