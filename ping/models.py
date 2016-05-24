from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Server(models.Model):
	
	url = models.CharField(max_length=50)
	user = models.ForeignKey(User)
	


