from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

index_response = "<h1> This is the homepage for the user_page app </h1>"

def index(request):
	return HttpResponse(index_response)