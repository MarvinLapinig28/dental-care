from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModel(UserAdmin):
     fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', 'postal','contact_number','profile_pic')}),
    )

    

admin.site.register(CustomUser,UserModel)
admin.site.register(Client)
admin.site.register(Featured)