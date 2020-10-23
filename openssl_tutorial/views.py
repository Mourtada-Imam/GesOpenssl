from django.shortcuts import render
from django.http import HttpResponse  
from .models import cert 
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
def form(request):
	return render(request,'openssl_tutorial/form.html')