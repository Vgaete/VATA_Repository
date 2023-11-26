from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import testModel
from .models import Object, Place


def index(request):
    template = loader.get_template("mainGUI/index.html")
    return render(request, "mainGUI/index.html", {})

def S2ndView(request):
    dataLugares = Place.objects.all()
    dataObjetos = Object.objects.all()
    receivedData = "0"
    print("lugares", dataLugares)
    return render(request, "mainGUI/2ndView.html", {'dataLugares': dataLugares, "dataObjetos": dataObjetos, "receivedData": receivedData})

def ShowData(request):
    dataLugares = Place.objects.all()
    dataObjetos = Object.objects.all()
    print("lugares", dataLugares)
    return render(request, "mainGUI/test.html", {'dataLugares': dataLugares, "dataObjetos": dataObjetos})

def mostrar_lugar(request, Place_id):
    Place_id=1
    lugar=Place.objects.get(pk=Place_id)
    return render(request,"2ndView.html",{"Place": lugar})
