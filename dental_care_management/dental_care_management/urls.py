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
    
    
    # PATIENT PATH
    path('Patient/Home',Patient_Views.HOME,name='patient_home'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

