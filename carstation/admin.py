from django.contrib import admin


#relative import

from .models import Carstation

admin.site.register(Carstation)