from django.http import HttpResponse
from django.shortcuts import render
from carstation.models import Carstation


# Create your views here.

def home_view(request,*args, **kwargs):
	objects = Carstation.objects.values()
	carstations = []

	for carstation in objects:
		carstations.append([str(carstation['name']),float(carstation['lengtitude']),float(carstation['longtitude'])])
		print(carstation['name'] + " " + str(carstation['lengtitude']))

	print(type(carstations))

	return render(request, "home.html",{'carstations':carstations})

def contact_view(request,*args, **kwargs):
	return render(request, "contact.html", {})

def ex_view(request,*args, **kwargs):
	return render(request, "ex.html", {})
