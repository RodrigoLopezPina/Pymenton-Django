from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.

def index(response):
    return render(response, "main/index.html")

def login(response):
    return render(response, "main/login.html")

def quienes_somos(response):
    return render(response, "main/quienes_somos.html")