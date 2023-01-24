from django.urls import path
from . import views

urlpatterns = [
    path('adminpage/',views.adminpage,name="adminpage"),
    path('sellerloginpage/',views.sellerloginpage,name="sellerloginpage"),
    path('sellerregistrationpage/',views.sellerregistrationpage,name="sellerregistrationpage"),
    path('saveplanterdetail/',views.saveplanterdetail,name="saveplanterdetail"),
    path('sellerlogin/',views.sellerlogin,name="sellerlogin"),
    path('servieces',views.servieces,name="servieces"),
    path('saveplantdetail/',views.saveplantdetail,name="saveplantdetail"),
    path('saveplantpage/',views.saveplantpage,name="saveplantpage"),
    path('sellerproductupdate/',views.sellerproductupdate,name="sellerproductupdate"),
    path('updateproduct<int:plantid1>',views.updateproduct,name="updateproduct"),
    path('updateproductpage/',views.updateproductpage,name="updateproductpage"),
    path('displayproducts/',views.displayproducts,name="displayproducts"),
    path('deletedata<int:deleteid>',views.deletedata,name="deletedata"),
    path('addtocart<int:singleid>',views.addtocart,name="addtocart"),
    path('editproduct<int:plantid>',views.editproduct,name="editproduct"),
    path('displayseller',views.displayseller,name="displayseller"),

]