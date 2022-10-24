from re import template
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Book, Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from.forms import CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 



# Create your views here.
def lindz(request): 
    return HttpResponse("Wassup!")

#Class based view
class MyViews(TemplateView): 
    template_name = 'index.html'

def book_list(request):
    book = Book.objects.all()
    return render(request, "book_list.html", {"books": book})
   
#View for all posts
def  Post_list(request):
    objects_list = Post.objects.all()
    paginator = Paginator(objects_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request, "index.html", {"page":page, "posts" : posts})

#View for single post
def post_detail (request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST': 
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.save()
    else :
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'new_comment': new_comment, 'comments': comments, 'comment_form': comment_form, 'post' : post})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login (request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("profile")
            else:
                messages.error(request, f"Invalid username or password.")
        else:
            messages.error(request, f"Devil is a LIAR!!")
    form = AuthenticationForm()
    return render(request, 'authenticate/login.html', context = {"form":form})


