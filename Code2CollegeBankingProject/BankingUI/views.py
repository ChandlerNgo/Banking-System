from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def createaccount(request):
    return render(request, 'createaccount.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')