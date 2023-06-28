from imaplib import _Authenticator
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Usuarios,Residuos,Registroresiduos
from django.db.models import Sum


def inicio(request): #Pagina inicio
    user=request.session['user']
    if(request.session['user']==None):
        request.session['user'] = None
    return render(request, 'inicio.html',{'usuario': user})

def somos(request): #Pagina Somos
    user = None
    user = request.session['user']
    return render(request,"somos.html",{'usuario': user})

def servicios(request): #Pagina Servicios
    user = None
    user = request.session['user']
    return render(request,"servicios.html",{'usuario': user})

def contacto(request): #Pagina Contacto
    user = None
    user = request.session['user']
    return render(request,"contacto.html",{'usuario': user})


def ranking(request): #Pagina Ranking
    user = None
    user = request.session['user']
    usuarios = Usuarios.objects.all()
    residuos=Residuos.objects.all()
    #Ordena los usuarios de la tabla por Total de puntos
    usuarios_ordenados = Usuarios.objects.annotate(total_puntos=Sum('registroresiduos__puntosobtenidos')).order_by('-total_puntos')
    for usuario in usuarios_ordenados:
        print(f"Usuario: {usuario.nombre}, Puntos totales: {usuario.total_puntos}")
    return render(request,"ranking.html",{'user':usuarios,'residuos':residuos,'ranking':usuarios_ordenados,'usuario': user})

def login(request): #Ventana de Login
    if request.method == 'POST':
        usuario = request.POST['usuario']
        request.session['user'] = usuario
        contrasena = request.POST['contrasena']
        try:
            usuario_obj = Usuarios.objects.get(usuario=usuario, contrasena=contrasena)
            return render(request, 'login_success.html', {'usuario': usuario_obj})
        except Usuarios.DoesNotExist:
            return render(request, 'login.html')
    return render(request, 'login.html')

def login_success(request, usuario_nombre): #Metodo para iniciar sesion
    usuario = Usuarios.objects.get(rut=usuario_nombre)
    return render(request, 'login_success.html', {'usuario': usuario})

def ingresar_residuos(request): #Pagina Ingresar residuos (Solo puede hacerlo el usuario o admnin)
    material=request.POST['material']
    kilos=int(request.POST['kilos'])
    puntaje_material=Residuos.objects.get(nombre=material)
    user = request.session['user']
   
    puntaje=int(puntaje_material.puntaje)
    puntos=puntaje*kilos
    r = Registroresiduos.objects.create(idr_id=puntaje_material,kilos=kilos,fecha="16-04-2023",puntosobtenidos=puntos,usuario_id='15.232.323-7')
    return redirect('/ranking.html')

def sesion(request): #Metodo para cerrar sesion
    request.session['user']=None
    user = request.session['user']
    return render(request, 'inicio.html', {'user': None})