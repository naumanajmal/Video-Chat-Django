from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'main/main.html', context = context)