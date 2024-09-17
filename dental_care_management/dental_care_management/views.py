from django.shortcuts import render,redirect, HttpResponse
from app.models import  CustomUser, Client
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages


def BASE(request):
    return render(request,'base.html')


def LOGIN(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == "POST":
        # Authenticate the user using your custom backend
        user = EmailBackEnd.authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )

        # If the user is authenticated successfully
        if user is not None:
            login(request, user)
            user_type = user.user_type

            # Redirect based on user type
            if user_type == '1':
                return redirect('dentist_home')  # For dentist users
            elif user_type == '2':
                return redirect('patient_home')  # For patient users
            else:
                messages.error(request, 'Email and Password are Invalid!')
                return redirect('login')
        else:
            # Handle failed authentication
            messages.error(request, 'Invalid email or password. Please try again.')
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')


def PROFILE(request):
    return render(request,'profile.html')

def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        postal = request.POST.get('postal')
        contact_number = request.POST.get('contact_number')

        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.email = email
            customuser.username = username
            customuser.address = address
            customuser.postal = postal 
            customuser.contact_number = contact_number
           


            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic !=None and profile_pic !="":
                 customuser.profile_pic = profile_pic
                
            customuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('profile')

        except:
            messages.error(request,'Failed to Update Your Profile !')
    return render(request,'profile.html')

def SIGNUP(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        postal = request.POST.get('postal')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Taken !')
            return redirect('signup')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is Already Taken !')
            return redirect('signup')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                address = address,
                contact_number=contact_number,
                postal=postal,
                user_type= 2
            )   
            user.set_password(password)
            user.save()

            client = Client (
                admin = user,
            )
            client.save()
            messages.success(request, user.first_name + " " + user.last_name + ' Are Successfully Added !')
            return redirect('login')
    return render(request,'signup.html')