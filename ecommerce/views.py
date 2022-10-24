from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

def lindi(request): 
    return HttpResponse("Wassup!")

#Class based view
class MyViews(View):
    def get(self, request):
        return HttpResponse('This is CBV')