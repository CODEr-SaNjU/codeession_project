from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"html_files/Home.htm")


def Tutorial(request):
    return render(request,"html_files/Tutorial.htm")

def Programs(request):
    return render(request,"html_files/programs.htm")

def contact(request):
    return render(request,'html_files/contact.htm')

def service(request):
    return render(request,"html_files/services.htm")

def sem1_1year(request):
    return render(request,"html_files/sem1_1year.htm")