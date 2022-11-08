from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
# from requests import request
from .forms import CreateUserForm

# Create your views here.


def registerView(request):
    form = CreateUserForm()
    if  request.method =='POST':
        if form.is_valid():
          form.save()
          username = form.cleaned_data['username']
          email = form.cleaned_data['email']
          password = form.cleaned_data['password']
          user = authenticate(username=username, password=password, email=email)
          login(request, user)
          messages.success(redirect, 'Account created successfully')
          return redirect('blog:profile')
    else:
        form = CreateUserForm()
    return render(request, 'registration/signup.html', {'form':form})

class UserEditView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy ("blog:profile")