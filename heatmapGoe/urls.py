"""heatmapGoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view
from pages.views import contact_view
from pages.views import ex_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #anmelden der seite
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('ex/', ex_view, name='ex'),
   

]
