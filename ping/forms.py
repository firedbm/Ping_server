from django import forms
import os

class Ping(forms.Form):
	servidor = forms.CharField(max_length=250, label='Server', required=True )
	def search_server(self):

		url = str(self.cleaned_data.get('servidor'))
		reponse = os.system("ping -c1 "+url)
		if not reponse:
			return "Server UP!"
		else:
			return 'Server Down!'




