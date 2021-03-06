from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evendo')
    data_criacao = models.DateTimeField(auto_now=True)
    local_evento = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M hrs')

    def get_data_input_evento(self): # para ser usado com datetime-local
        return self.data_evento.strftime('%Y-%m-%d %H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
    def get_evento_proximo(self):
        data_atual = self.data_evento - timedelta(hours=1)
        if datetime.now() > data_atual:
            return True
        else:
            return False