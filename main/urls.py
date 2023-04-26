from django.urls import path
from .views import home, search, detail,login
from django.shortcuts import render
from django.template import RequestContext
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("search", search, name="search"),
    path("<slug>", detail, name="detail"),
    path("<login>", login, name="login"),
    path('register/', RegisterUser.as_view(), name='register'),



]

def handler404(request, *args, **argv):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response