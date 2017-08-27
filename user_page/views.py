from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

index_response = "<h1> This is the homepage for the user_page app </h1>"

def index(request):
	# returns a simple string of data, which is parsed and displayed as HTML by the browser
	return HttpResponse(index_response)