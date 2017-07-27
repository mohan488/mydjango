# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

def post_post(request):
    return HttpResponse("<h1>POST</h1>")

def post_get(request):
    context = {
    "title" : "Detail"
    }
    #return render(request, "index.html",{})
    return render(request, "index.html", context)
def post_put(request):
    #return HttpResponse("<h1>PUT</h1>")
    # if request.user.is_authenticated():
    #     context = {
    #         "title" : "my user login"
    #     }
    # else:
    #     context = {
    #         "title" : "list"
    #     }

    context = {
        "title" : "list"
    }
    
    #return render(request, "index.html",{})
    return render(request, "index.html", context)

def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")

def post_list(request):
    return HttpResponse("<h1>LISt</h1>")
