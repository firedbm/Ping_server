from django.conf.urls import url
from .views import create_user, logout_user

urlpatterns = [
    url(r'^create_user', create_user, name= "create_user"),
    url(r'^logout', logout_user, name= "logout"),
]