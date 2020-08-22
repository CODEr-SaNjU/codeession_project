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