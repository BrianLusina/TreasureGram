from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^$', view=views.index, name="index"),
    url(regex=r'([0-9]+)/$', view=views.detail, name="detail"),
    url(regex=r'post_url/$', view=views.post_treasure, name="post_treasure")
]
