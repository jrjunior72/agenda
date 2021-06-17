"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('eventos/<titulo_evento>/', views.local_evento),
    path('agenda/', views.lista_eventos),
    path('agenda/evento/', views.evento), # redireciona para página de cadastro de evento
    path('agenda/evento/submit', views.submit_evento),
    # path('', views.index) #uma maneira de redirecionar a url
    path('', RedirectView.as_view(url='/agenda/')), #outra maneira de redirecionar a url
    path('login/', views.login_user), # redirecionar para página de login
    path('login/submit', views.submit_login), # redireciona para submit_login
    path('logout/', views.logout_user) # logout do usuário
]
