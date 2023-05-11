from django.shortcuts import render

def inicio(request):
    context = {}
    return render(request, 'inicio.html', context)

