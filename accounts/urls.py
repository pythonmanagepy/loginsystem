from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [

path('admin', admin.site.urls),
path('user_login/admin', admin.site.urls),
path('',views.home,name="home"),
path('signup/',views.register,name="register"),

path('user_login',views.user_login,name="user_login"),
path('seller_dashboard',views.seller_dashboard,name="seller_dashboard"),
path('customer_dashboard',views.customer_dashboard,name="customer_dashboard"),
path('user_logout',views.user_logout,name="user_logout"),
path('edit_profile',views.edit_profile,name="edit_profile"),
path('details',views.details,name="details"),


]
