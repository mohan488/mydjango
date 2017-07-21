# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

def post_post(request):
    return HttpResponse("<h1>POST</h1>")

def post_get(request):
    return HttpResponse("<h1>GET</h1>")

def post_put(request):
    return HttpResponse("<h1>PUT</h1>")

def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")

def post_list(request):
    return HttpResponse("<h1>LISt</h1>")
