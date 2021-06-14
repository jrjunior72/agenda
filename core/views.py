from django.shortcuts import render, HttpResponse #redirect


# Create your views here.
from core.models import Evento


# def local_evento(request, titulo_evento):
#     context = {}
#     context['local_evento'] = Evento.local_evento(titulo=titulo_evento)
# #    return HttpResponse(Evento.filter(titulo=titulo_evento))
#     return HttpResponse(context)

# # uma maneira de redirecionar uma url
# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    # retorna a lista de eventos do usuário loggado
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    # dados = {'eventos':evento}
    # return render(request, 'agenda.html', dados)
    # retorna o evento 1
    # evento = Evento.objects.get(id=1)
    # retorna toda a lista de eventos
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
