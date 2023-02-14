from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def links(reuqest):
    return HttpResponse('links')
