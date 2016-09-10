# Treasure Gram

Small sample Django application on Treasures discovered by some adventurous treasurers.

## Project Structure
    |--TreasureGram/
        init__.py
        settings.py
        urls.py -> project url dispatcher
        wsgi.py
    |--main_app/
        migrations/
            __init__.py/
        __init__.py
        urls.py-> app url dispatcher
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    .gitignore
    db.sqlite3
    manage.py
    README.md
    requirements.txt

## URL Dispatcher Best Practices

### Refactoring the project's URLs dispatcher
First remove the index/ from the regex and match an empty path to load the view

``` python
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main_app.urls'))
]
```
> This will still perform the same function as before when the url(r'^index/', views.index)
 
## The App URLs Dispatcher

It is best practice to have a project URL dispatcher and an app URL dispatcher. The Projects URL dispatcher is handling all the requests but it is best practice to funnel all the app specific requests to an **App's URL dispatcher**
Thus in the project's url dispatcher we need to include the app's url dispatcher

### Creating the App's url dispatcher

First import `url` from `django.conf.urls` then import the views

``` python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^$', view=views.index)
]
```

## URL-View Template Process

The client will request for a specific url, the URL dispatcher will match this to a correct view and the *View* will collect needed data and render the *Template*. The Template simply defines the URL to be rendered.

You will need to create a templates directory in every app that you will have in your project.
First register your app in the projects `settings` file.

In the `settings.py` file, you will find a list called `INSTALLED_APPS`, register your application name there.
Then render the template in the views like so:

``` python
# Create your views here.
def index(request):
    name = "Gold Nugget"
    value = 1000.00
    context = {'treasure_name': name,
               'treasure_val': value}
    return render(request=request, template_name="index.html", context=context)
```
> this dynamic data(`context`)will be passed to the render function which will pass it to the template.
 
 Access your data like this in the index.html
``` html
<h1>TreasureGram</h1>
<p>{{ treasure_name }}</p>
<p>{{ treasure_val }}</p>
```

## Models

This defines the data structure and communicates with the database. It is a good way to organize the data.
Create your tables here that will define your tables to be mapped with Django's ORM to an SQL database.


## The admin

The admin site allows you to perform administrative tasks. These tasks can be performed by authorized users only. To do this you will need to create superusers with this command:

``` bash
python manage.py createsuperuser
```

You will then have to enter a username, email and password

After which you can go to `localhost:8000/admin` and log in using your credentials.

After logging in you will not be able to see your models, this is because you have to register them first. The registration is done using `admin.py`