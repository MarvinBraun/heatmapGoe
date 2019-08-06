from django.http import HttpResponse
from django.shortcuts import render
from carstation.models import Carstation
import os
import dotenv
import sys
import json
import environ
from django.core.wsgi import get_wsgi_application

# Create your views here.

def home_view(request,*args, **kwargs):
	objects = Carstation.objects.all()
	carstations = []
	carstations2 = []
	labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	#Koordinaten für Google Maps

	for index, carstation in enumerate(objects):
		label = labels[index % len(labels)]
		carstations.append([float(carstation.lengtitude),float(carstation.longtitude),float(carstation.bookings),carstation.name,label])
		#print(carstation['name'] + " " + str(carstation['lengtitude']))
	carstations = json.dumps(carstations)
	print(type(carstations))

	#Autovermietungen Objekte für Tabelle
	carstations2 = Carstation.objects.values()

	#Google Api Key
	env = environ.Env(API=str)
	environ.Env.read_env()
	api = env('API')
	api_key = os.getenv('API')
	api = []
	api.append(api_key)
	key = "https://maps.googleapis.com/maps/api/js?key="+api_key+"&libraries=visualization&callback=initMap"

	#print(dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname("Secret_Keys")), '.env')))


	return render(request, "home.html",{'carstations':carstations, 'carstations2':carstations2,'key':key})

def contact_view(request,*args, **kwargs):
	return render(request, "contact.html", {})

def start_view(request,*args, **kwargs):
	return render(request, "start.html", {})
