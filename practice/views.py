from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world!. This is Aryush Web. This is a Home page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello world!. This is Aryush Web. This is a About page")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello world!. This is Aryush Web. This is a contact page")
    return render(request, 'website/contact.html')

def services(request):
    # return HttpResponse("Hello world!. This is Aryush Web. This is a contact page")
    return render(request, 'website/services.html')