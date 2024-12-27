from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
def thello(request):
    template=loader.get_template('hello.html')
    return HttpResponse(template.render())
