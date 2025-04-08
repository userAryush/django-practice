from django.shortcuts import render
from .models import AppVariety

# Create your views here.

def all_app(request):
    apps = AppVariety.objects.all() #array aauxa
    
    return render(request, 'practice_app/all_app.html', {'apps': apps}) 