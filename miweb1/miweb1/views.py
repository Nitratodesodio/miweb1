from django.shortcuts import render

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
    return render(request,"ranking.html")

