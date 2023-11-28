from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import testModel
from .models import Object, Place


def index(request):
    template = loader.get_template("mainGUI/index.html")
    return render(request, "mainGUI/index.html", {})

def S2ndView(request, lugar):
    dataLugares = Place.objects.all()
    dataObjetos = Object.objects.all()
    print("lugares", dataLugares)
    return render(request, "mainGUI/2ndView.html", {'dataLugares': dataLugares, "dataObjetos": dataObjetos, "receivedData": lugar})

def ShowData(request):
    dataLugares = Place.objects.all()
    dataObjetos = Object.objects.all()
    print("lugares", dataLugares)
    return render(request, "mainGUI/test.html", {'dataLugares': dataLugares, "dataObjetos": dataObjetos})

def mostrar_lugar(request, Place_id):
    Place_id=1
    lugar=Place.objects.get(pk=Place_id)
    return render(request,"2ndView.html",{"Place": lugar})

def guardar_lugar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        location = request.POST.get('location')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')
        categoria = request.POST.get('categoria')

        nuevo_lugar = Place(placeName=nombre, location=location, descripcion=descripcion, placeImage=imagen, placeCategory=categoria)
        nuevo_lugar.save()
        print(nombre, location,descripcion, imagen, categoria)

        return redirect( 'index')  # Puedes renderizar una página de confirmación o redirigir a otra vista
    else:
        return redirect( 'mostrar_formulario')  # Si la solicitud no es POST, muestra el formulario nuevamente



def mostrar_formulario(request):
    return render(request, 'formulario.html')

def home(request):
    return render(request, 'home.html')

def ayuda(request):
    return render(request, 'paginadeayuda.html')
