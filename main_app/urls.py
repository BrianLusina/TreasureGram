from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(regex=r'^$', view=views.index, name="index"),
    url(regex=r'([0-9]+)/$', view=views.detail, name="detail"),
    url(regex=r'post_url/$', view=views.post_treasure, name="post_treasure"),
    url(regex=r'user/(\w+)/$', view=views.profile, name="profile"),
    url(regex=r'^login/$', view=views.login_view, name="login"),
]


# sends any URL that matches media/ to a built in Django view called static.serve
if settings.DEBUG:
    urlpatterns += [
        url('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
