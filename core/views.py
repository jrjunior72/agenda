from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# def local_evento(request, titulo_evento):
#     context = {}
#     context['local_evento'] = Evento.local_evento(titulo=titulo_evento)
# #    return HttpResponse(Evento.filter(titulo=titulo_evento))
#     return HttpResponse(context)

# # uma maneira de redirecionar uma url
# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválida")
    return redirect('/')

@login_required(login_url='/login/')

def lista_eventos(request):
    # retorna a lista de eventos do usuário loggado
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    # dados = {'eventos':evento}
    # return render(request, 'agenda.html', dados)
    # retorna o evento 1
    # evento = Evento.objects.get(id=1)
    # retorna toda a lista de eventos
    # evento = Evento.objects.all()
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
