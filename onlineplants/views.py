from django.shortcuts import render,redirect
from onlineplants.models import details
from backend.models import cdetails,plantdetail

from django.contrib.auth import login,authenticate

# Create your views here.
def index(request):
    return render(request,'index.html')
def sellerpage(request):
    return render(request,'sellerpage.html')
def home(request):
    return redirect(index())
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def loginpage(request):
    return render(request,'seller-login.html')
def savedata(request):
    if request.method=="POST":
        vname=request.POST.get('Name')
        vemail=request.POST.get('Email')
        vphone=request.POST.get('Phone')
        vimage=request.FILES['Image']
        object1=details(
            name=vname,
            email=vemail,
            phone=vphone,
            image=vimage

        )
        object1.save()
        return redirect(index)
def registration(request):
    return render(request,'registration.html')
# def userlogin(request):
#     if request.method=="POST":
#         us=request.POST.get('username')
#         ps=request.POST.get('password')
#         if sellerdb.objects.filter(username__contains=us).exists():
#             user=authenticate(username=us,password=ps)
#             if user is not None:
#                 login(request,user)
#                 return redirect(index)
#             else:
#                 return redirect(login)
#         else:
#             return redirect(login)
def savecontact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        nm=request.POST.get('num')
        add=request.POST.get('address')
        objectc=cdetails(
            cname=na,
            cphone=nm,
            cadd=add

        )
        objectc.save()
        return redirect(index)
def displayplantsforsale(request):
    plantsd=plantdetail.objects.all()
    return render(request,'display.html',{'plantsd':plantsd})
def updateproductpage(request):
    plantsu=plantdetail.objects.all()
    return render(request,'updateproduct.html',{'plantsu':plantsu})
def search(request):
    if "search" in request.GET:
        search=request.GET["search"]
        seplants=plantdetail.objects.filter(pnamecontains=search)
    else:
        seplants = plantdetail.objects.all()
    context={
        'seplants':seplants
    }
    return render(request,'sdisplay.html',context)
