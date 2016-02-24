
from django.conf.urls import url,include,url
from django.contrib import admin

urlpatterns = [
	url(r'^' , include('apps.home.urls')),
    url(r'^admin/', admin.site.urls),

]
