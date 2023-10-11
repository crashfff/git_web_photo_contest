from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def page_user(request):
    template = loader.get_template('page_user.html')
    return HttpResponse(template.render())


def photo(request):
    template = loader.get_template('photo.html')
    return HttpResponse(template.render())
