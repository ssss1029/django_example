# django_example
A sample project in Django. Users are able to log in and keep track of their favorite books. Users can also sign up for the website and log in easily.

This is a super barebones sample project made with Django. It has two endpoints:
 - `/login/`
 - `/user_page/`

The `/user_page/` endpoint is only accessible for logged-in users. Users can sign up and login at `/login/` and then access their `/user_page/`. The home endpoint `/` redirects to one of the other two endpoints based on weather or not the user is logged in.

In order to run:

Clone the repository:
```
cd <some directory where you want this to be>
git init
git remote add origin https://github.com/ssss1029/django_example.git
git pull origin master
```

Make sure Django is installed, if you haven't already:
```
pip install django
```

Run the server:
```
python manage.py runserver
```

The site should be live at `http://127.0.0.1/`. You will probably need to create a new user in order to use the website using the `/login/` endpoint.
