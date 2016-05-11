from django.shortcuts import render, redirect
from .forms import LoginForm, UserForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_user(request):
	if request.user.is_authenticated():
		return redirect('ping:ping_server')
	data = LoginForm(request.POST or None)

	if data.is_valid():
		data.login(request)
		return redirect('ping:ping_server')
	context ={
		'form': data,
		}
	return render(request,'login.html',context)

def create_user(request):
	data = UserForm(request.POST or None)
	if data.is_valid():
		data.create_user()
		return redirect('login_user')
	context = {
	'form': data,
	}
	return render(request,'create_user.html',context)

@login_required
def logout_user(request):
	logout(request)
	return redirect('login_user')

