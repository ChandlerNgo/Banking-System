from django.shortcuts import render
from django.http import HttpResponse
from .FormFunctions.createaccount import savenewaccountinfo
from .models import Customer,BankInfo,Transactions

def index(request):
    # if username doesnt exist print("This username doesn't exist")
    # if password doesnt exist print("This password is wrong, try forgot password")
    return render(request,'index.html')

def createaccount(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        birthday = request.POST["birthday"]
        username = request.POST["firstname"]
        pinnumber = request.POST["pinnumber"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]
        if password != confirmpassword:
            return HttpResponse("Your password and confirming password are not the same")
        newcustomer = Customer(first_name = firstname,last_name = lastname,birthday = birthday,email = email)
        newcustomer.save()
        newbankinfo = BankInfo(pin_number = pinnumber, username = username,password = password) 
        newbankinfo.save()
        # id is not included in the newbankinfo, so it throws a mean error
    return render(request,'createaccount.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def account(request):
    return render(request,'account.html')

def changeaccountinfo(request):
    return render(request,'changeaccountinfo.html')

def changemoney(request):
    return render(request,'changemoney.html')

# add required field into the end of html forms after testing