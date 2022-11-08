from django import views
from django.urls import path

from blog.views import  book_list, Post_list, post_detail, profileView, loginView, logoutView, contactView, aboutView



app_name = 'blog'

urlpatterns = [
    path("contact/", contactView, name="contact"),
    path("about/", aboutView, name="about"),
    path("login/", loginView, name="login"),
    path('profile/', profileView, name='profile'),
    path('profile/', logoutView, name="logout"),
    path("book_list/", book_list),
    path("", Post_list ),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name= 'post_detail'),
    ]