from django.conf.urls import url
from .views import search_ping

urlpatterns = [
    url(r'^ping_server', search_ping, name= "ping_server"),
]