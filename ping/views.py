from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Ping

# Create your views here.
@login_required
def search_ping(request):
	
	form = Ping(request.POST or None)
	context= {
	'form': form,
	}
	if form.is_valid():
		context["servidor"] = form.search_server()
	

	return render(request, 'ping.html', context)
