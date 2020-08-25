from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('Tutorials',views.Tutorial,name="Tutorial"),
    path('Programs',views.Programs,name="Programs"),
    path('contact',views.contact,name="contact"),
    path('services',views.service,name="services"),
    path('1_semester',views.sem1_1year,name="1_semester"),
    path('2_semester',views.sem2_1year,name="2_semester"),
    path('civil_2nd',views.civil_2nd ,name="civil_2nd"),
    path('cse_2nd',views.cse_2nd ,name="cse_2nd"),
    path('me_2nd',views.me_2nd ,name="me_2nd"),
    path('el_2nd',views.el_2nd ,name="el_2nd"),
    path('ee_2nd',views.ee_2nd ,name="ee_2nd"),
    path('it_2nd',views.it_2nd ,name="it_2nd"),
]