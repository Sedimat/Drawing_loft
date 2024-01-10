from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'Drawing/base.html')


def table(request):
    return render(request, 'Drawing/table.html')