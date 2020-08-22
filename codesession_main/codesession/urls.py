from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('Tutorials',views.Tutorial,name="Tutorial"),
    path('Programs',views.Programs,name="Programs"),
    path('contact',views.contact,name="contact"),
]