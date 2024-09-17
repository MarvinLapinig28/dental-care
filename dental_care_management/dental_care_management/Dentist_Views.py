from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from app.models import Featured, CustomUser ,Client
from django.contrib import messages




@login_required(login_url='/')
def HOME(request):
    return render(request,'Dentist/home.html')

def FEATURED(request):
    if request.method == "POST":
        featured_photo = request.FILES.get('featured_photo')
        featured_name = request.POST.get('featured_name')
        full_price = request.POST.get('full_price')
        discounted_price = request.POST.get('discounted_price')
        
        featured = Featured(
            name = featured_name,
            featured_photo = featured_photo,
            full_price = full_price,
            discounted_price = discounted_price,
        )
        featured.save()
        messages.success(request,'Featured Are Successfully Added !')
        return redirect('featured_add')
    return render(request,'Dentist/featured.html')

def VIEW(request):
    featured = Featured.objects.all()
    context = {
        'featured':featured,
    }
    return render(request,'Dentist/view_featured.html',context)

def EDIT_FEATURED(request,id):
    featured = Featured.objects.get(id = id)
    context = {
        'featured':featured,
    }
    return render(request,'Dentist/edit_featured.html',context)

def UPDATE_FEATURED(request):
    if request.method == "POST":
        featured_photo = request.FILES.get('featured_photo')
        featured_name = request.POST.get('featured_name')
        featured_id = request.POST.get('featured_id')
        full_price = request.POST.get('full_price')
        discounted_price = request.POST.get('discounted_price')
        
        featured = Featured.objects.get(id = featured_id)
        featured.name = featured_name
        featured.full_price = full_price
        featured.discounted_price = discounted_price
        
        if featured_photo !=None and featured_photo !="":
            featured.featured_photo = featured_photo
        featured.save()
        messages.success(request,'Featured Are Successfully Updated !')
        return redirect('view_featured')
    return render(request,'Dentist/view_featured.html')

def DELETE_FEATURED(request,id):
    featured = Featured.objects.get(id=id)
    featured.delete()
    messages.success(request,'Featured Are Successfully Deleted! ')
    return redirect('view_featured')

def VIEW_PATIENT(request):
    client = Client.objects.all()
    context = {
        'client':client,
    }
    return render(request,'Dentist/view_patient.html',context)