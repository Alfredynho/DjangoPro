
from django.conf.urls import url
from django.contrib import admin
from .views import IndexView
#Urls de la aplicacion home
urlpatterns = [
	url(r'^$' , IndexView.as_view())
]
