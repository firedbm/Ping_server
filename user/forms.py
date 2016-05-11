from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(label='Usuario', required=True)
	password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		user = authenticate(username=username, password=password)

		if not user:
			self.add_error('password','incorrect password')
			raise forms.ValidationError('User or Password misstake')

	def login(self,request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		user = authenticate(username=username, password=password)

		if user:
			login(request, user)


class UserForm(forms.Form):

	first_name = forms.CharField(label='First Name',required=True)
	last_name = forms.CharField(label='Last Name',required=True)
	username = forms.CharField(label='Username', required=True)
	email = forms.CharField(label='Email', required=True, widget=forms.EmailInput)
	password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)

	def create_user(self):

		new_user = User.objects.create_user(self.cleaned_data.get('username'),
                                            self.cleaned_data.get('email'),
                                            self.cleaned_data.get('password'))
		new_user.first_name = self.cleaned_data.get('first_name')
		new_user.last_name = self.cleaned_data.get('last_name')
		new_user.save()

	def clean(self):

		if User.objects.filter(username=self.cleaned_data.get('username')).exists():

			raise forms.ValidationError('User is already taken')

			



