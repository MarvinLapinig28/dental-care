from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from app.models import Featured, CustomUser , Client_Request , Client , Client_Invoice

def HOME(request):
    superuser = CustomUser.objects.filter(is_superuser=True).first() 
    featured = Featured.objects.all()
    context = {
        'superuser':superuser,
        'featured':featured,
    }
    return render(request,'Patient/home.html',context)

def PATIENT_REQUEST(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        payment = request.POST.get('payment')
        featured_id = request.POST.get('featured_id')
        
        client = Client.objects.get(admin=user_id)
        client.save()
        
        featured = Featured.objects.get(name=featured_id)
        client_request = Client_Request(
            featured_id = featured,
            client_id = client,
            address = address,
            contact_number = contact_number,
            payment = payment,
        )
        client_request.save()
        return redirect ('patient_home')
    
def VIEW_REQUEST(request):
    client = Client.objects.filter(admin=request.user.id)
    for i in client:
        client_id = i.id
        
        client_request = Client_Request.objects.filter(client_id=client_id).order_by('-id')
        context = {
        'client_request':client_request,
    }
    return render(request,'Patient/view_request.html',context)

def VIEW_SCHEDULE(request):
    client = Client.objects.filter(admin=request.user.id)
    for i in client:
        client_id = i.id
        
        client_invoice = Client_Invoice.objects.filter(client_id=client_id).order_by('-id')
        context = {
        'client_invoice':client_invoice,
    }
    return render(request,'Patient/view_schedule.html',context)