from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import testModel
from .models import Object, Place

def index(request):
    template = loader.get_template("mainGUI/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def S2ndView(request):
    template = loader.get_template("mainGUI/2ndView.html")
    context = {}
    return HttpResponse(template.render(context, request))

def ShowData(request):
    dataLugares = Place.objects.all()
    dataObjetos = Object.objects.all()
    print("lugares", dataLugares)
    return render(request, "mainGUI/test.html", {'dataLugares': dataLugares, "dataObjetos": dataObjetos})