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

def sem2_1year(request):
    return render(request,"html_files/2nd_sem.htm")

def civil_2nd(request):
    return render(request,"html_files/civil_2nd.htm")

def cse_2nd(request):
    return render(request,"html_files/cse_2nd.htm")

def ee_2nd(request):
    return render(request,"html_files/ee_2nd.htm")

def el_2nd(request):
    return render(request,"html_files/el_2nd.htm")

def me_2nd(request):
    return render(request,"html_files/me_2nd.htm")

def it_2nd(request):
    return render(request,"html_files/it_2nd.htm")

def civil_3rd(request):
    return render(request,"html_files/civil_3rd.htm")

def cse_3rd(request):
    return render(request,"html_files/cse_3rd.htm")

def ee_3rd(request):
    return render(request,"html_files/ee_3rd.htm")

def el_3rd(request):
    return render(request,"html_files/el_3rd.htm")

def me_3rd(request):
    return render(request,"html_files/me_3rd.htm")

def it_3rd(request):
    return render(request,"html_files/it_3rd.htm")