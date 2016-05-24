from django.conf.urls import url
from .views import create_servers, ajax_server, ajax_delete

urlpatterns = [
    url(r'^ping_server', create_servers ,name= "ping_server"),
    url(r'^ajax/$', ajax_server ,name= "ajax"),
    url(r'^ajax/delete/$', ajax_delete ,name= "ajax_delete"),
]