from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import MateriMatematika


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def materimtk(request):
    template = loader.get_template('materimtk.html')
    materi = MateriMatematika.objects.all()
    context = {
        'dataMateri': materi,
    }
    return HttpResponse(template.render())

def sejarahmtk(request):
    template = loader.get_template('sejarahmtk.html')
    return HttpResponse(template.render())

def tokohmtk(request):
    template = loader.get_template('tokohmtk.html')
    return HttpResponse(template.render())

def soallatihan(request):
    template = loader.get_template('soallatihan.html')
    return HttpResponse(template.render())

def webpembahasan(request):
    template = loader.get_template('webpembahasan.html')
    return HttpResponse(template.render())