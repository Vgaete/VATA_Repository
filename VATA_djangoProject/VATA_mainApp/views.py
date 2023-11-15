from django.http import HttpResponse
from django.template import loader

from .models import testModel

def index(request):
    template = loader.get_template("mainGUI/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def S2ndView(request):
    template = loader.get_template("mainGUI/2ndView.html")
    context = {"valor1": "valor1", "valor2": "valor2", "valor3": 0}
    return HttpResponse(template.render(context, request))