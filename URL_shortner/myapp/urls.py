from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page),
    path('<slug:short_url>', views.redirect_url)
]
