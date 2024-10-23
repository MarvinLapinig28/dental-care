from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, Dentist_Views, Patient_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name='base'),

    #LOGIN PATH
    path('', views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='doLogout'),
    path('SignUp', views.SIGNUP,name='signup'),

    # PROFILE UPDATE
    path('profile',views.PROFILE,name='profile'),
    path('Profile/Update',views.PROFILE_UPDATE,name='profile_update'),
    

    # DENTIST PATH
    path('Dentist/Home',Dentist_Views.HOME,name='dentist_home'),
    path('Featured/Add',Dentist_Views.FEATURED,name='featured_add'),
    path('Featured/View',Dentist_Views.VIEW,name='view_featured'),
    path('Featured/Edit/<str:id>',Dentist_Views.EDIT_FEATURED,name="edit_featured"),
    path('Featured/Update',Dentist_Views.UPDATE_FEATURED,name='update_featured'),
    path('Featured/Delete/<str:id>',Dentist_Views.DELETE_FEATURED,name='delete_featured'),
    path('View/Patient',Dentist_Views.VIEW_PATIENT,name='view_patient'),
    path('View/Patient/Request',Dentist_Views.VIEW_REQUEST,name='view_request'),
    path('Dentist/approve_request/<str:id>',Dentist_Views.REQUEST_APPROVE,name='approve_request'),
    path('Dentist/reject_request/<str:id>',Dentist_Views.REJECT_REQUEST,name='reject_request'),
    path('Dentist/Patient/Invoice',Dentist_Views.PATIENT_INVOICE,name='patient_invoice'),
    
    
    # PATIENT PATH
    path('Patient/Home',Patient_Views.HOME,name='patient_home'),
    path('Patient/Request',Patient_Views.PATIENT_REQUEST,name='patient_request'),
    path('Path/View/Request',Patient_Views.VIEW_REQUEST,name='view_request_patient'),
    path('Patient/View/Schedule',Patient_Views.VIEW_SCHEDULE,name='view_schedule'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

