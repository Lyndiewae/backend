from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from requests import request

# Create your views here.
def loginView(request):
    return render(request, "authenticate/login.html")