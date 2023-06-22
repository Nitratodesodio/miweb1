from imaplib import _Authenticator
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Usuarios,Residuos,Registroresiduos
from django.db.models import Sum

#AGREGANDO UN COMENTARIO PARA GITHUB
#AGREAGNDO UN COMENTARIO PARTE 2
def inicio(request):
    context = {}
    return render(request, 'inicio.html', context)

def somos(request):
    return render(request,"somos.html")

def servicios(request):
    return render(request,"servicios.html")

def contacto(request):
    return render(request,"contacto.html")


def ranking(request):
    usuarios = Usuarios.objects.all()
    residuos=Residuos.objects.all()
    usuarios_ordenados = Usuarios.objects.annotate(total_puntos=Sum('registroresiduos__puntosobtenidos')).order_by('-total_puntos')
    for usuario in usuarios_ordenados:
        print(f"Usuario: {usuario.nombre}, Puntos totales: {usuario.total_puntos}")
    return render(request,"ranking.html",{'user':usuarios,'residuos':residuos,'ranking':usuarios_ordenados})

def login(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']
        try:
            usuario_obj = Usuarios.objects.get(usuario=usuario, contrasena=contrasena)
            return render(request, 'login_success.html', {'usuario': usuario_obj})
        except Usuarios.DoesNotExist:
            return render(request, 'login.html')
    return render(request, 'login.html')

def login_success(request, usuario_id):
    usuario = Usuarios.objects.get(rut=usuario_id)
    return render(request, 'login_success.html', {'usuario': usuario})
