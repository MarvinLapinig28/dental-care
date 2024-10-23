from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        ('1','Dentist'),
        ('2', 'Patient'),
    )


    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic',null=True,blank=False)
    address = models.TextField()
    postal = models.TextField()
    gender = models.CharField(max_length=100)
    contact_number = models.TextField()
    
class Client(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    valid_id = models.ImageField( upload_to="media/uploads", null=True, blank=False)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class Featured(models.Model):
    name = models.CharField(max_length=100)
    featured_photo = models.ImageField(upload_to="media/uploads",null=True,blank=False)
    full_price = models.TextField()
    discounted_price = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Client_Request(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.TextField()
    contact_number = models.TextField()
    status = models.IntegerField(default=0)
    featured_id = models.ForeignKey(Featured, on_delete=models.DO_NOTHING)
    payment = models.CharField(max_length=100)

    def __str__(self):
        return self.client_id.admin.first_name + " " + self.client_id.admin.last_name
    
class Client_Invoice(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.client_id.admin.first_name + " " + self.client_id.admin.last_name


