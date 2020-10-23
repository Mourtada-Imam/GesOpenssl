from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class cert(models.Model):
	nomDomain = models.CharField(max_length=100)
	nomOrg= models.CharField(max_length=100)
	deprt= models.CharField(max_length=100)
	ville = models.CharField(max_length=100)
	region=models.CharField(max_length=100)
	code= models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	
