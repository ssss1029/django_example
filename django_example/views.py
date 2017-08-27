from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

index_response = "<h1> This is the main website homepage </h1>"
def index(request):
	return HttpResponse(index_response)