# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# For more information on models, see the following site:
#	https://docs.djangoproject.com/en/1.11/topics/db/models/
class Book(models.Model):
	title  = models.CharField(max_length=400)
	author = models.CharField(max_length=400)

	def __str__(self):
		return "Book: " + self.title + ", by: " + self.author
