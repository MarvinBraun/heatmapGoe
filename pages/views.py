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
	labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	#carRental JS= genutzt für getMarker / getPoints
	carRentalsJS = _getCarRentalsForJS()
	#carRentalHTML= genutzt für ListGroup
	carRentalsHTML = _getCarRentalsForHTML()
	#Java API KEY
	key = _readAPIKey()

	return render(request, "home.html",{'carRentalsJS': carRentalsJS, 'carRentalsHTML': carRentalsHTML,'key':key})

def contact_view(request,*args, **kwargs):
	return render(request, "contact.html", {})

def start_view(request,*args, **kwargs):
	return render(request, "start.html", {})






def _getCarRentalsForJS():
	labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	objects = Carstation.objects.all()
	carRentals = []

	for index, carRental in enumerate(objects):
		label = labels[index % len(labels)]
		carRentals.append([
			 float(carRental.lengtitude),
			 float(carRental.longtitude),
			 float(carRental.bookings),
			carRental.name, label
			 ])

	return json.dumps(carRentals)


def _getCarRentalsForHTML():
	labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	# Autovermietungen Objekte für Tabelle
	carRentals = Carstation.objects.values()

	for index, carRental in enumerate(carRentals):
		carRental['label'] = labels[index % len(labels)]

	return carRentals

def _readAPIKey():
	env = environ.Env(API=str)
	environ.Env.read_env()
	api = env('API')
	api_key = os.getenv('API')
	api = []
	api.append(api_key)
	key = "https://maps.googleapis.com/maps/api/js?key="+api_key+"&libraries=visualization&callback=initMap"

	return key