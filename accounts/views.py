from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import register_table,state
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.method== "POST":
		fname=request.POST["first"]
		last=request.POST["last"]
		un=request.POST["username"]
		pwd=request.POST["password"]
		ctn=request.POST["contactno"]
		tp=request.POST["utype"]

		usr=User.objects.create_user(un,un,pwd)
		usr.first_name=fname 
		usr.last_name=last 
		if tp=="sell":
			usr.is_staff=True
		usr.save()

		reg = register_table(user=usr,contact_number=ctn)
		reg.save();

	return render(request,"register.html")

def home(request):
	return render(request,"base.html")

def user_login(request):
	response=HttpResponse()
	if request.method=="POST":
		un=request.POST["username"]
		pwd=request.POST["password"]

		user=authenticate(username=un,password=pwd)
		if user:
			login(request,user)

			if user.is_superuser:
				return HttpResponseRedirect('/admin')
			if user.is_staff:
				return HttpResponseRedirect('/seller_dashboard')
			if user.is_active:
				return HttpResponseRedirect('/customer_dashboard')
				


		else:
			return render(request,"base.html",{"status":"invalid username or password"})
		return response
@login_required
def seller_dashboard(request):
	return render(request,"seller_dashboard.html")

@login_required
def customer_dashboard(request):
	return render(request,"customer_dashboard.html")
	
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/')

def edit_profile(request):
	context={}
	data=register_table.objects.get(user__id=request.user.id)
	context["data"]=data
	if request.method=="POST":


		fn=request.POST["fname"]
		ln=request.POST["lname"]
		em=request.POST["email"]

		con=request.POST["contact"]
		age=request.POST["age"]
		city=request.POST["city"]
		about=request.POST["about"]


		

		usr= User.objects.get(id=request.user.id)
		usr.first_name=fn  
		usr.last_name=ln 
		usr.email=em 
		usr.save()

		data.contact_number=con   
		data.about=about  
		data.city=city
		data.age=age  
		data.save()
		context["status"]= "Changes saved successfully"


	return render(request,"edit_profile.html",context)


def details(request):

	data=state.objects.all().filter(user__id=request.user.id)
	context={}
	context["data"]=data
	return render(request,"details.jinja",context)

