from django.conf.urls import url, include
from . import views

urlpatterns = [
	#/login/
	url(r'^$', views.index, name="user_page_index")
]