"""
URL configuration for miweb1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
     path('', views.inicio, name='inicio'),
     path('inicio.html', views.inicio),
     path('somos.html', views.somos, name='somos'),
     path('contacto.html', views.contacto, name='contacto'),
     path('ranking.html', views.ranking, name='ranking'),
     path('servicios.html', views.servicios, name='servicios'),
     path('login', views.login, name='login'),
     path('login_success', views.login_success, name='login_success'),
     path('ingresar_residuos', views.ingresar_residuos, name='ingresar_residuos'),
     path('sesion', views.sesion, name='sesion'),
     path('registrarse', views.registrarse, name='registrarse'),
     path('registro', views.registro, name='registro'),

        
]
