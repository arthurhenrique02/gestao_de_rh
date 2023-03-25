from django.shortcuts import render
from django.http import HttpResponse

# definir view home
# request como argumento para poder pegar a requisição do usuário
def home(request):
    return HttpResponse("Ola mundo!")
