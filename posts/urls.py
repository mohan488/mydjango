from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^post/$', views.post_post),
    url(r'^get/$', views.post_get),
    url(r'^put/$', views.post_put),
    url(r'^delete/$', views.post_delete),
    url(r'^list/$', views.post_list),
]
