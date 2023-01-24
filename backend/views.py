from django.shortcuts import render,redirect
from backend.models import sellerdb,plantdetail
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def adminpage(request):
    return render(request,'admin.html')
def sellerloginpage(request):
    return render(request,'seller-login.html')
def sellerregistrationpage(request):
    return render(request,'sellerregistration.html')
def servieces(request):
    return render(request,'servieces.html')
def saveplanterdetail(request):
    if request.method=="POST":
        name=request.POST.get('name')
        psw=request.POST.get('psw')
        add=request.POST.get('add')
        sellerobject=sellerdb(sellername=name,sellerpassword=psw,selleraddress=add)
        sellerobject.save()
        return render(request,'seller-login.html')
def sellerlogin(request):
    if request.method == "POST":
        sn=request.POST.get('sname')
        sp=request.POST.get('spsw')
        if sellerdb.objects.filter(sellername=sn,sellerpassword=sp).exists():
            request.session['sellername']=sn
            return redirect(adminpage)
        else:
            return render(request,'seller-login.html')

def  saveplantpage(request):
    return render(request,'sellerpage.html')
def saveplantdetail(request):
    if request.method=="POST":
        pname1=request.POST.get('hpname')
        pdetail1=request.POST.get('hpdetail')
        pprice1=request.POST.get('hpprice')
        sellercode1=request.POST.get('sellercode')

        pimage1=request.FILES['hpimage']
        plantobject=plantdetail(pname=pname1, pdetail=pdetail1,pprice=pprice1,pimage=pimage1,sellercode=sellercode1)
        plantobject.save()
        return redirect(sellerproductupdate)

def updateproduct(request,plantid1):
    if request.method == "POST":
        pname1 = request.POST.get('hpname')
        pdetail1 = request.POST.get('hpdetail')
        pprice1 = request.POST.get('hpprice')
        try:
            im = request.FILES['hpimage']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=plantdetail.objects.get(id=plantid1).pimage

        plantdetail.objects.filter(id=plantid1).update(pname=pname1, pdetail=pdetail1, pprice=pprice1,pimage=file)
        return redirect(sellerproductupdate)

def sellerproductupdate(request):
    plants=plantdetail.objects.all()
    return render(request,'cred.html',{'plants':plants })

def updateproductpage(request,plantid):
    plants = plantdetail.objects.get(id=plantid)
    return render(request,'cred.html',{'plants':plants})
def displayproducts(request):
    return render(request,'display.html')
def editproduct(request,plantid):
    plantsid = plantdetail.objects.get(id=plantid)
    return render(request,'updateproduct.html',{'plantsid':plantsid})
def deletedata(request,deleteid):
    plants = plantdetail.objects.get(id=deleteid)
    plants.delete()
    return redirect(sellerproductupdate)
def addtocart(request,singleid):
    if request.method=="POST":
        splants =plantdetail.objects.filter(id=singleid)
        return render(request,'singleproduct.html',{'splants':splants})
def displayseller(request):
       code=plantdetail.objects.filter(sellercode='5').values()
       context={
            'code':code
       }
       return render(request,'displayseller.html',context)
