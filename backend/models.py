from django.db import models
# Create your models here.
class sellerdb(models.Model):
    sellername=models.CharField(max_length=100,null=True,blank=True)
    sellerpassword=models.CharField(max_length=100,null=True,blank=True)
    selleraddress = models.CharField(max_length=100, null=True, blank=True)
class cdetails(models.Model):
    cname=models.CharField(max_length=100,null=True,blank=True)
    cphone=models.CharField(max_length=100,null=True,blank=True)
    cadd=models.CharField(max_length=100, null=True, blank=True)
class plantdetail(models.Model):
    pname=models.CharField(max_length=100,null=True,blank=True)
    pdetail=models.CharField(max_length=100,null=True,blank=True)
    pprice=models.CharField(max_length=100, null=True, blank=True)
    sellercode=models.CharField(max_length=100, null=True, blank=True)
    pimage=models.ImageField(upload_to="profile")
