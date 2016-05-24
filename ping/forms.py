from django import forms
from .models import Server
from django.contrib.auth.models import User
import validators


class Ping(forms.Form):
	server = forms.CharField(max_length=250, label='Server', required=True )


		

	def create_server(self,request):
		user = request.user
		url = str(self.cleaned_data.get('server'))
		serverS=Server.objects.filter(url=url)
		if serverS:
			self.add_error('server','Url already exist')
		else:
			if validators.url('https://'+url) or validators.url('http://'+url):
				server = Server.objects.create(url=url,user=user)
				server.save()
			else:
				self.add_error('server','Incorrect url')
			
		

	

		 




