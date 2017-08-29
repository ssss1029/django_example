# Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Models
from .models import Book
from login.models import User

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		not_authenticated_html = "<h1>Welcome to the user page. You are not authenticated</h1>"
		not_authenticated_html += "<h2><a href='/login'> You can log in here. </a></h2>"
		not_authenticated_html += "<p>In order to see cool stuff, you'll need to log in.</p>"
		return HttpResponse(not_authenticated_html)
	else:
		# Do stuff with authenticated user
		if len(request.user.favorited_books.all()) == 0:
			# The user has not favorited any books yet.
			template = loader.get_template('user_page/index.html')
			context = { 
				'logged_in_user' : request.user.first_name + " " + request.user.last_name,
				'no_books_message' : 'You have no books yet! :('
			}
			return HttpResponse(template.render(context, request))			
		else:
			template = loader.get_template('user_page/index.html')
			context = { 
				'logged_in_user' : request.user.first_name + " " + request.user.last_name,
				'books' : request.user.favorited_books.all()
			}
			return HttpResponse(template.render(context, request))
