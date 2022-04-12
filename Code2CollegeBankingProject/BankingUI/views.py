from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def createaccount(request):
    template = loader.get_template('createaccount.html')
    return HttpResponse(template.render())

def forgotpassword(request):
    template = loader.get_template('forgotpassword.html')
    return HttpResponse(template.render())

def account(request):
    template = loader.get_template('account.html')
    return HttpResponse(template.render())

def createaccountinfo(request):
    template = loader.get_template('createaccountinfo.html')
    return HttpResponse(template.render())

def changemoney(request):
    template = loader.get_template('changemoney.html')
    return HttpResponse(template.render())