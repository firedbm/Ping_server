from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Ping
from .models import Server
from django.http import JsonResponse, Http404
import os

# Create your views here.
@login_required
def create_servers(request):
	form = Ping(request.POST or None)
	context= {
	'form': form,
		}
	if form.is_valid():
		form.create_server(request)
	return render(request, 'ping.html', context)



def show_server(request):
	user = request.user
	server = Server.objects.filter(user = user)
	return server


def search_server(url):
		url = str(url)
		reponse = os.system("ping -c1 "+url)
		if not reponse:
			return "Server UP!"
		else:
			return 'Server Down!'

@login_required
def ajax_server(request):
	if not request.is_ajax():
		raise Http404
	user = request.user
	server = Server.objects.filter(user=user)
	data = {}
	data['server'] = []
	for i in server:

		data['server'].append((i.id, i.url, search_server(i.url)))
		
	return JsonResponse(data)

@login_required
def ajax_delete(request):
	if not request.is_ajax():
		raise Http404
	id = request.POST.get("id")
	server = Server.objects.get(id=id)
	server.delete()
	data ={
	'status':True
	}
	return JsonResponse(data)


