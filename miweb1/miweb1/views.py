from imaplib import _Authenticator
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Usuarios,Residuos,Registroresiduos
from django.db.models import Sum


def inicio(request):
    """
    Vista para mostrar la página de inicio.
    - Si el usuario ha iniciado sesión, muestra la página 'inicio.html' con el nombre de usuario.
    - Si el usuario no ha iniciado sesión, redirige al usuario a la página de inicio de sesión.
    """
    user = request.session['user']
    if request.session['user'] is None:
        request.session['user'] = None
    return render(request, 'inicio.html', {'usuario': user})


def somos(request):
    """
    Vista para mostrar la página 'somos.html'.
    - Recupera el nombre de usuario de la sesión.
    - Muestra la página 'somos.html' con el nombre de usuario.
    """
    user = request.session['user']
    return render(request, "somos.html", {'usuario': user})


def servicios(request):
    """
    Vista para mostrar la página 'servicios.html'.
    - Recupera el nombre de usuario de la sesión.
    - Muestra la página 'servicios.html' con el nombre de usuario.
    """
    user = request.session['user']
    return render(request, "servicios.html", {'usuario': user})


def contacto(request):
    """
    Vista para mostrar la página 'contacto.html'.
    - Recupera el nombre de usuario de la sesión.
    - Muestra la página 'contacto.html' con el nombre de usuario.
    """
    user = request.session['user']
    return render(request, "contacto.html", {'usuario': user})


def ranking(request):
    """
    Vista para mostrar la página de ranking.
    - Recupera el nombre de usuario de la sesión.
    - Obtiene todos los usuarios y residuos de la base de datos.
    - Ordena los usuarios por el total de puntos obtenidos.
    - Muestra la página 'ranking.html' con los usuarios, residuos y ranking ordenado, junto con el nombre de usuario.
    """
    user = request.session['user']
    usuarios = Usuarios.objects.all()
    residuos = Residuos.objects.all()
    usuarios_ordenados = Usuarios.objects.annotate(total_puntos=Sum('registroresiduos__puntosobtenidos')).order_by('-total_puntos')
    return render(request, "ranking.html", {'user': usuarios, 'residuos': residuos, 'ranking': usuarios_ordenados, 'usuario': user})


def login(request):
    """
    Vista para manejar la ventana de inicio de sesión.
    - Si la solicitud es POST, verifica las credenciales de inicio de sesión.
      - Si las credenciales son válidas, muestra la página 'login_success.html' con el objeto de usuario.
      - Si las credenciales son inválidas, muestra la página 'login.html' nuevamente.
    - Si la solicitud es GET, muestra la página 'login.html'.
    """
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

def login_success(request):
    """
    Vista para mostrar la página de éxito de inicio de sesión.
    - Recupera el nombre de usuario de la sesión.
    - Muestra la página 'login_success.html' con el nombre de usuario.
    """
    usuario = request.session['user']
    return render(request, 'login_success.html', {'usuario': usuario})


def ingresar_residuos(request):
    """
    Vista para procesar el formulario de ingreso de residuos.
    - Recupera el material y los kilos ingresados en el formulario.
    - Obtiene el objeto de Residuos correspondiente al material.
    - Recupera el nombre de usuario de la sesión.
    - Obtiene el objeto de Usuarios correspondiente al nombre de usuario.
    - Calcula los puntos obtenidos según el puntaje del material y los kilos ingresados.
    - Crea un nuevo objeto de Registroresiduos con los datos obtenidos.
    - Redirige al usuario a la página de ranking.
    """
    material = request.POST['material']
    kilos = int(request.POST['kilos'])
    puntaje_material = Residuos.objects.get(nombre=material)
    user = request.session['user']
    usersesion = Usuarios.objects.get(usuario=user)
    puntaje = int(puntaje_material.puntaje)
    puntos = puntaje * kilos
    r = Registroresiduos.objects.create(idr_id=puntaje_material, kilos=kilos, fecha="16-04-2023", puntosobtenidos=puntos, 
    usuario_id=usersesion.rut)
    return redirect('/ranking.html')


def sesion(request):
    """
    Vista para cerrar sesión.
    - Establece el nombre de usuario en la sesión como None.
    - Recupera el nombre de usuario de la sesión y establece la variable de usuario como None.
    - Muestra la página 'inicio.html' con el usuario establecido como None.
    """
    request.session['user'] = None
    user = request.session['user']
    return render(request, 'inicio.html', {'user': None})


def registrarse(request):
    """
    Vista para mostrar la página de registro.
    - Recupera el nombre de usuario de la sesión.
    - Muestra la página 'registrarse.html' con el nombre de usuario.
    """
    user = request.session['user']
    return render(request, "registrarse.html", {'usuario': user})

def registro(request):
    """
    Vista para procesar el formulario de registro.
    - Si la solicitud es POST, recupera los datos del formulario y crea un nuevo objeto de Usuarios con ellos.
      - Guarda el objeto en la base de datos.
      - Muestra la página 'inicio.html'.
    - Si la solicitud es GET, muestra la página 'inicio.html'.
    """
    if request.method == 'POST':
        nombre = request.POST['nombre']
        rut = request.POST['rut']
        username = request.POST['username']
        direccion = request.POST['direccion']
        password = request.POST['password']
        usuario = Usuarios(nombre=nombre, rut=rut, usuario=username, direccion=direccion, contrasena=password)
        usuario.save()
        return render(request, 'inicio.html')
    return render(request, 'inicio.html')
