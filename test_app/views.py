from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 0;
    if not 'letters' in request.session:
        request.session['letters'] = get_random_string(length=14)
    return render(request, 'index.html')

def generate(request):
    if request.method == "POST":
        request.session['letters']= get_random_string(length=14)
        request.session['counter'] += 1
    return redirect('/')
    
def reset(request):
    if request.method == "GET":
        request.session['counter'] = 0
    return redirect('/')

# Create your views here.
