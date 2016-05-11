
from django.conf.urls import url , include
from django.contrib import admin
from user.views import login_user


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ping/', include('ping.urls', namespace="ping")),
    url(r'^$', login_user, name="login_user"),
    url(r'^user/', include('user.urls', namespace="user")),
]
