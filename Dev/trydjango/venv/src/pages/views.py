from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello Django</h1>") # string of HTML code
def about_view(*args, **kwargs):
    return HttpResponse("<h1>This is the about page!</h1>")

