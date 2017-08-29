from django.db import models
from django.contrib.auth.models import AbstractUser
from user_page.models import Book

# Here, we are extending the default user model in order to add some extra functionality to
# the User object.
class User(AbstractUser):
    bio            = models.TextField(null=True, max_length=500, blank=True)
    location       = models.CharField(null=True, max_length=30, blank=True)
    birth_date     = models.DateField(null=True, blank=True)
    
    """
    See https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/
    	for what exactly a many-to-many field is. Essentially what this line says 
    	is that any book can be favorited by many users, and different users can
    	have different lists of favorited books. Note the import up top for Book.
	"""
    favorited_books = models.ManyToManyField(Book, null=True, blank=True)

    def __str__(self):
    	return "User: " + self.first_name + " " + self.last_name

