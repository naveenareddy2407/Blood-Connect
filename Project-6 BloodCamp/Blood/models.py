from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,User
from django.db import models

class patient(models.Model):
    Full_Name =models.CharField(max_length=50)
    Phone =models.TextField(max_length=12)
    Email=models.EmailField()
    Blood_type=models.CharField(max_length=50)
    def __str__(self):
        return self.Full_Name
class donardetail(models.Model):
    Full_Name =models.OneToOneField(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=40,blank=True,null=True)
    Phone =models.DecimalField(max_digits=12,decimal_places=0)
    Blood_type=models.CharField(max_length=50)
    Address=models.TextField(max_length=50,blank=True,null='')
    current_Address=models.TextField(max_length=50,blank=True,null='')
    Drinking=models.BooleanField(default=False)
    Date_of_Birth=models.DateField(blank=True,null=True)
    Smoking=models.BooleanField(default=False)
    Health_issue=models.CharField(max_length=50,blank=True,null='')
    def __str__(self):
        return self.Name
