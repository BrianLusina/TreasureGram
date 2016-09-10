# Treasure Gram

Small Django application

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



        
    
    