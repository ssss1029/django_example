from django.conf.urls import url, include
from . import views

urlpatterns = [
	# /user_page/
	url(r'^$', views.index, name="user_page_index"),

	# /user_page/processChange
	url(r'^processChange/', views.processChange, name="process_change")
]