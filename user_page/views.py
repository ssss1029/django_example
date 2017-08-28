# Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		not_authenticated_html = "<h1>Welcome to the user page. You are not authenticated</h1>"
		not_authenticated_html += "<h2><a href='/login'> You can log in here. </a></h2>"
		not_authenticated_html += "<p>In order to see cool stuf, you'll need to log in.</p>"
		return HttpResponse(not_authenticated_html)
	else:
		# Do stuff with authenticated user
		pass
