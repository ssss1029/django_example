# Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Models
from .models import Book
from login.models import User

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

def processChange(request):
	if not request.user.is_authenticated:
		return HttpResponse("Error: Not Authenticated")

	# Check if it is a remove type request or add type request
	if request.POST.get("book_title", False) and request.POST.get("book_author", False):
		# The request is an add request
		book_title  = request.POST.get("book_title", False)
		book_author = request.POST.get("book_author", False)

		new_book = Book(title=book_title, author=book_author)
		new_book.save()
		request.user.favorited_books.add(new_book)

		return HttpResponse("ok")			
	elif request.POST.get("book_pk", False):
		# The request is a delete request
		primary_key = request.POST.get("book_pk", False)
		request.user.favorited_books.remove(Book.objects.get(pk=primary_key))
		Book.objects.get(pk=primary_key).delete()
		return HttpResponse("ok")
	else:
		return HttpResponse("Error: Invalid POST parameters")			
