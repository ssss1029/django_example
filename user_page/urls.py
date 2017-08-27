from django.conf.urls import url
from . import views

"""
This is not the main urls module. See django_example.urls module
This module handles all of the routing within the /user_page/... address
"""

urlpatterns = [
	# Redirects any request for /user_page/ to the index view
	url(r'^$', views.index, name="index"),
]