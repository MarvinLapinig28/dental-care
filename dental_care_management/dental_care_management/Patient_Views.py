from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from app.models import Featured, CustomUser

def HOME(request):
    featured = Featured.objects.all()
    context = {
        'featured':featured,
    }
    return render(request,'Patient/home.html',context)