from django.shortcuts import render

def inicio(request):
    context = {}
    return render(request, 'inicio.html', context)

def somos(request):
    return render(request,"somos.html")

