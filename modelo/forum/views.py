from django.http import HttpResponse
from django.shortcuts import render
import hashlib

from .models import *

def index(request):
    context = {'teste': 'shflkjnvlkrej'}
    return render(request, 'forum/base.html', context)

def login(request):
    if request.method == "POST":
        #print(request.POST['sen'])
        #print(hashlib.sha512(bytes(request.POST['sen'], 'utf-8')).hexdigest())
        
        usu = usuario.objects.filter(
            nome = request.POST['usu'],
            senha = hashlib.sha512(bytes(request.POST['sen'], 'utf-8')).hexdigest()
        )
        if len(usu) == 1:
            request.session['nome'] = request.POST['usu']
            print('LOGADO')
        else:
            print('ERRO')
    context = {}
    return render(request, 'forum/login.html', context)

def cadastrar(request):
    pass

def ini_thread(reuqest):
    if request.method == "POST":
        pass

    