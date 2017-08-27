from django.conf.urls import url, include
from django.contrib import admin
from . import views

"""
This is the file that Django looks at first when the user requests "/" (http://127.0.0.1/)
    See the following in order to learn more about how incoming requests are exactly
    parsed: https://docs.djangoproject.com/en/1.11/topics/http/urls/#how-django-processes-a-request

This module was specified in our django_example/settings.py file
"""

urlpatterns = [
    # Tells Django to redirect us to the views.index function if the incoming request is for '/'
	url(r'^$', views.index, name="index"),

    # Tells Django to redirect us to the default admin module that Django gives us if
    # the incoming request is for '/admin/'
    url(r'^admin/', admin.site.urls),

    # Tells Django to look in the 'user_page.urls' file in order to process any requests that 
    # are of the format /user_page/<anything>/... 
    # This lets us offload all the work of routing requests that come to any sub-directory of /user_page
    # into the user_page.urls file, which is located at "/django_example/user_page/urls"
    # include() is a Django-provided function. Note we imported it at the top of this file.
    url(r'^user_page/', include('user_page.urls')),
]
