from django.shortcuts import render
# from myapp.models import form1, form2, form3

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def form1(request):
    return render(request, 'form1.html', {})

def form2(request):
    if request.method == 'POST':
        ...
    
    return render(request, 'form2.html', {})

def form3(request):
    if request.method == 'POST':
        ...
    return render(request, 'form3.html', {})

def result(request):
    if request.method == 'POST':
        ...
    return render(request, 'result.html', {})