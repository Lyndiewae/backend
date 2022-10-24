from django.urls import path
from blog.views import lindz
from blog.views import MyViews, book_list, Post_list, post_detail



app_name = 'blog'

urlpatterns = [
    path("book_list/", book_list),
    path("", Post_list ),
    path("about/", MyViews.as_view(), name= "home"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name= 'post_detail'),
    ]