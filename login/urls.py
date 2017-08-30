from django.conf.urls import url, include
from . import views

urlpatterns = [
	# /login/
	url(r'^$', views.index, name="login_index"),

	# I know this is weird but this is an example app, but this kind of a weird url would not 
	# usually be used in production
	# /login/logout/
	url(r'^logout/', views.logout_view, name="login_logout")
]