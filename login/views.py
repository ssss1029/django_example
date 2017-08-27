# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	if request.method == "GET": 
		# Give back the login page
		template = loader.get_template('login/index.html')
		context = {}
		return HttpResponse(template.render(context, request))
	elif request.method == "POST":
		# Actually log the user object in
		pass
	else:
		# There was a mistake
		return HttpResponse("<h1> This endpoint does not support request type: " 
			+ request.method 
			+ " </h1>")