from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
) 
from django.contrib.auth.decorators import login_required
from .models import cert 
import subprocess
import os
# Create your views here.

def home (request): 
    
    return render(request, 'openssl_tutorial/home.html')
def about (request):
    return render(request,'openssl_tutorial/about.html')
def ope (request):
    return render(request,'openssl_tutorial/ope.html')
def ope2(request):
    return render(request,'openssl_tutorial/ope2.html')
def ope3(request):
    return render(request,'openssl_tutorial/ope3.html')
def ope4(request):
    return render(request,'openssl_tutorial/ope4.html')
def ope5(request):
    return render(request,'openssl_tutorial/ope5.html')
def ope6(request):
    return render(request,'openssl_tutorial/ope6.html')
def ope7(request):
    return render(request,'openssl_tutorial/ope7.html')

def ope8(request):
    return render(request,'openssl_tutorial/ope8.html')
def ope9(request):
    return render(request,'openssl_tutorial/ope9.html')
def ope10(request):
    return render(request,'openssl_tutorial/ope10.html')    
@login_required
def form(request):
    #return render(request,'openssl_tutorial/form.html')
    if request.POST:
       os.popen('openssl req -x509 -newkey rsa:4096 -days 365 -nodes -keyout ca-key.pem -out ca-cert.pem').read()
       output = os.popen('cat ca-cert.pem').read()
       return render(request,'openssl_tutorial/cert.html', {'output': output})

    return render(request,'openssl_tutorial/form.html')
@login_required
def csr(request):
    #return render(request,'openssl_tutorial/form.html')
    if request.POST:
       os.popen('openssl req -newkey rsa:4096 -nodes -keyout server-key.pem -out server-req.pem').read()
       output = os.popen('cat server-key.pem').read()
       return render(request,'openssl_tutorial/res.html', {'output': output})

    return render(request,'openssl_tutorial/csr.html')
def server_req(request):
    #return render(request,'openssl_tutorial/form.html')
    if request.POST:
       os.popen('openssl x509 -req -in server-req.pem -days 60 -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem -extfile server-ext.cnf').read()
       os.popen('openssl x509 -in server-cert.pem -noout -text').read()
       output = os.popen('cat server-req.pem').read()
       return render(request,'openssl_tutorial/serv.html', {'output': output})

    return render(request,'openssl_tutorial/server_req.html')