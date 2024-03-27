from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva

def home_view(request):
    return render(request, "aplicacion/home.html")
def list_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {'reservas': reservas}
    return render(request, "aplicacion/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"reservas": reservas_del_usuario}
    return render(request, "aplicacion/list.html", contexto_dict) 


def create_view(request, nombre_de_usuario, destino):
    reserva = Reserva.objects.create(nombre_de_usuario=nombre_de_usuario, destino=destino)

    return HttpResponse(f"Resultado: {reserva}")