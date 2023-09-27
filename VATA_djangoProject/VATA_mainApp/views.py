from django.http import HttpResponse
from django.template import loader

from .models import testModel

def index(request):
    template = template = loader.get_template("mainGUI/index.html")
    context = {}
    return HttpResponse(template.render(context, request))
