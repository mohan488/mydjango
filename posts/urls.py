from django.conf.urls import url
from django.contrib import admin
from .views import (post_post, post_get, post_put,
      post_delete, post_list)


urlpatterns = [
    url(r'^post/$', post_post),
    url(r'^get/$', post_get),
    url(r'^put/$', post_put),
    url(r'^delete/$', post_delete),
    url(r'^list/$', post_list),
]
