from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
A view is something that handles giving the request data back. 
We mentioned this file in the django_exmample.urls module
"""

index_response = "<h1> This is the main website homepage </h1>"
def index(request):
	return HttpResponse(index_response)