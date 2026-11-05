"""
URL configuration for traveloutfit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from travelapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather',views.weather,name="weather"),
    path('',views.index),
    path('userregistration',views.userregistration,name="userregistration"),
    path('supplierreg',views.supplierreg,name="supplierreg"),
    path('accomodationreg',views.accomodationreg,name="accomodationreg"),
    path('login',views.login,name="login"),

    path('adminHome',views.adminHome,name="adminHome"),
    path('adminUser',views.adminUser,name="adminUser"),
    path('adm_app_user',views.adm_app_user,name="adm_app_user"),
    path('adminSupplier',views.adminSupplier,name="adminSupplier"),
    path('adminAccomodation',views.adminAccomodation,name="adminAccomodation"),
    path('adm_app_supplier',views.adm_app_supplier,name="adm_app_supplier"),
    path('adm_app_acc',views.adm_app_acc,name="adm_app_acc"),
    path('adminProducts',views.adminProducts,name="adminProducts"),
    path('adminApproveProduct',views.adminApproveProduct,name="adminApproveProduct"),
    path('adminBookings',views.adminBookings,name="adminBookings"),
    path('adminFeedbacks',views.adminFeedbacks,name="adminFeedbacks"),
    path('adminVWAcc',views.adminVWAcc,name="adminVWAcc"),
    path('adminVwRooms',views.adminVwRooms,name="adminVwRooms"),
    path('adminAccBookings',views.adminAccBookings,name="adminAccBookings"),

    path('supplierHome',views.supplierHome,name="supplierHome"),
    path('supplierAdd',views.supplierAdd,name="supplierAdd"),
    path('addqty',views.addqty,name="addqty"),
    path('supplierBooking',views.supplierBooking,name="supplierBooking"),
    path('supplierFeedback',views.supplierFeedback,name="supplierFeedback"),

    path('userHome',views.userHome,name="userHome"),
    path('userProduct',views.userProduct,name="userProduct"),
    path('userSearch',views.userSearch,name="userSearch"),
    path('userSearchAcc',views.userSearchAcc,name="userSearchAcc"),
    path('userCart',views.userCart,name="userCart"),
    path('remove_fromCart',views.remove_fromCart,name="remove_fromCart"),
    path('payment',views.payment,name="payment"),
    path('userBookings',views.userBookings,name="userBookings"),
    path('userAddFeedback',views.userAddFeedback,name="userAddFeedback"),
    path('userProfile',views.userProfile,name="userProfile"),
    path('userAccomodations',views.userAccomodations,name="userAccomodations"),
    path('userVwRooms',views.userVwRooms,name="userVwRooms"),
    path('userBookRoom',views.userBookRoom,name="userBookRoom"),
    path('userAccPay',views.userAccPay,name="userAccPay"),
    path('userRoomBookings',views.userRoomBookings,name="userRoomBookings"),


    path('accHome',views.accHome,name="accHome"),
    path('accPost',views.accPost,name="accPost"),
    path('accBookings',views.accBookings,name="accBookings"),
    path('accAcceptBooking',views.accAcceptBooking,name="accAcceptBooking"),


    
]
