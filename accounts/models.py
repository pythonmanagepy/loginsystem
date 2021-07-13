from django.db import models
from django.contrib.auth.models import User


class register_table(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	contact_number=models.IntegerField()
	age=models.CharField(max_length=250,null=True,blank=True)
	city=models.CharField(max_length=250,null=True,blank=True)
	about=models.TextField(blank=True,null=True)
	

class state(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	dt=models.DateField(blank=True,null=True)
	
	debit=models.IntegerField(default=0)
	credit=models.IntegerField(default=0)

	billno=models.IntegerField(blank=True,null=True)
	fnam=models.CharField(max_length=50,blank=True,null=True)





	def __str__(self):
		return self.user.username




# Create your models here.
