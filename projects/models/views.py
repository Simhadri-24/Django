from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import name
def models(request):
    mymembers=name.objects.all().values()
    template=loader.get_template('mymembers.html')
    context={'mymembers':mymembers,}
    return HttpResponse(template.render(context,request))
