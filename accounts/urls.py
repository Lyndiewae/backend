from django.urls import path
from .import views




app_name = 'accounts'

urlpatterns = [
    path("accounts/login", views.loginView, name = 'login'),
    path("", ),
    path("",),
    path("",),
]