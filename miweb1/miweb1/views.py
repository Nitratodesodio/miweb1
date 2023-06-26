from imaplib import _Authenticator
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Usuarios,Residuos,Registroresiduos
from django.db.models import Sum

#AGREGANDO UN COMENTARIO PARA GITHUB
#AGREAGNDO UN COMENTARIO PARTE 2
def inicio(request):
    user=request.session['user']
    if(request.session['user']==None):
        request.session['user'] = None
        print("Sin usuario")
    elif(request.session['user']!=None):
        print("Otro usuario")
    
    return render(request, 'inicio.html',{'usuario': user})

def somos(request):
    user = None
    user = request.session['user']
    
    return render(request,"somos.html",{'usuario': user})

def servicios(request):
    user = None
    user = request.session['user']
    return render(request,"servicios.html",{'usuario': user})

def contacto(request):
    user = None
    user = request.session['user']
    if(request.session['user'] == None):
       print("No hay usuario")
   
    return render(request,"contacto.html",{'usuario': user})


def ranking(request):
    user = None
    user = request.session['user']
    usuarios = Usuarios.objects.all()
    residuos=Residuos.objects.all()
    
    print("Usuario" ,user, "-------********************************")
    usuarios_ordenados = Usuarios.objects.annotate(total_puntos=Sum('registroresiduos__puntosobtenidos')).order_by('-total_puntos')
    for usuario in usuarios_ordenados:
        print(f"Usuario: {usuario.nombre}, Puntos totales: {usuario.total_puntos}")
    return render(request,"ranking.html",{'user':usuarios,'residuos':residuos,'ranking':usuarios_ordenados,'usuario': user})

def login(request):
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

def login_success(request, usuario_nombre):
    usuario = Usuarios.objects.get(rut=usuario_nombre)
    
   
  
    return render(request, 'login_success.html', {'usuario': usuario})

def ingresar_residuos(request):
    material=request.POST['material']
    kilos=int(request.POST['kilos'])
    puntaje_material=Residuos.objects.get(nombre=material)
    user = request.session['user']
    print("Usuario" ,user, "-------********************************")
    id_m=puntaje_material.idr
    puntaje=int(puntaje_material.puntaje)
    
        
    puntos=puntaje*kilos
    print("kilos:" ,kilos, "-------")
    print("materialid:", id_m, "-------")
    print("puntaje:", puntos, "-------")

    r = Registroresiduos.objects.create(idr_id=puntaje_material,kilos=kilos,fecha="16-04-2023",puntosobtenidos=puntos,usuario_id='15.232.323-7')
    return redirect('/ranking.html')

def sesion(request):
    request.session['user']=None
    user = request.session['user']
    return render(request, 'inicio.html', {'user': None})