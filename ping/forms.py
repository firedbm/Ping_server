from django import forms
import os

class Ping(forms.Form):
	servidor = forms.CharField(max_length=250, label='Servidor', required=True )
	def search_server(self):

		dato= self.cleaned_data.get('servidor')
		reponse = os.system("ping -c1 "+str(dato))
		if not reponse:
			return "Servidor Disponible"
		else:
			return 'Servidor no Disponible'




