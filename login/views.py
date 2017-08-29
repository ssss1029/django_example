# Imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
# Authentication imports
from django.contrib.auth import authenticate, login
from .models import User

def index(request):
	if request.method == "GET": 
		# Check if the user is already logged in
		if not request.user.is_authenticated:		
			# Give back the login page
			template = loader.get_template('login/index.html')
			context = {}
			return HttpResponse(template.render(context, request))
		else:
			# Redirect back to the home page
			return redirect('/user_page/')
	elif request.method == "POST":
		# Check if this is a signup request
		if request.POST.get('first_name', False) and request.POST.get('last_name', False) and request.POST.get('email', False) and request.POST.get('username', False) and request.POST.get('password', False) and request.POST.get('confirm_password', False):
			# The request was a signup request
			if request.POST['password'] == request.POST['confirm_password']:
				# Make the user object that we will save to the db
				# See: https://docs.djangoproject.com/en/1.11/ref/contrib/auth/#django.contrib.auth.models.User 
				# 	for more information. If, for a specific use case, we need a new field for the user (e.g. Boolean 
				#   for "paid"), we can exend this user default user object and create a sublcass.
				user = User.objects.create_user(request.POST['username'])
				user.set_password(request.POST['password'])  ## Using set_password() is important. In order to be secure, this is what
															 ## we need to do to make sure that raw passwords aren't stored 
															 ## in the database. See 
															 ## https://docs.djangoproject.com/en/1.11/topics/auth/default/#changing-passwords 
															 ## for more info
				user.email      = request.POST['email']
				user.first_name = request.POST['first_name']
				user.last_name  = request.POST['last_name']
				user.save()

				login(request, user)

				# Success redirect
				return redirect('/user_page/')
			else:
				# Failure redirect
				template = loader.get_template('login/index.html')
				context = { "error" : "Incorrect username or password. Please try again." }
				return HttpResponse(template.render(context, request))
		# Check if this is a login request
		elif request.POST.get('username', False) and request.POST.get('password', False):
			# The request was a login request
			username = request.POST['username']
			password = request.POST['password']
			
			user = authenticate(request, username=username, password=password)

			if user is not None:
				# Correct username / password
				login(request, user)

				# Success redirect
				return redirect('/user_page/')
			else:
				# Failure redirect
				template = loader.get_template('login/index.html')
				context = { "error" : "Incorrect username or password. Please try again." }
				return HttpResponse(template.render(context, request))
		else: 
			# Invalid request
			return HttpResponse("<h1> Invalid request </h1>")
	else:
		# There was a mistake
		return HttpResponse("<h1> This endpoint does not support request type: " 
			+ request.method 
			+ " </h1>")