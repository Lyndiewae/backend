from django.urls import path
from ecommerce.views import MyViews, lindi



urlpatterns = [
    path("", lindi ),
    path('about/', MyViews.as_view())
    ]
