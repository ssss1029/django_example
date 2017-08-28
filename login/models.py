from django.db import models
from django.contrib.auth.models import AbstractUser

# Here, we are extending the default user model in order to add some extra functionality to
# the User object.
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
