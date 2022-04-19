from django.shortcuts import render
from django.http import HttpResponse
from .FormFunctions.createaccount import savenewaccountinfo
from .models import Customer,BankInfo,Transactions
from django.db.utils import IntegrityError

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
    return render(request,'index.html')

def createaccount(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        birthday = request.POST["birthday"]
        username = request.POST["username"]
        pinnumber = request.POST["pinnumber"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]

        if password != confirmpassword:
            user = {
                "response":"Your password and confirming password are not the same"
            }
            render(request,'createaccount.html',user)

        newcustomer = Customer(first_name = firstname,last_name = lastname,birthday = birthday,email = email)
        newcustomer.save()
        newbankinfo = BankInfo(pin_number = pinnumber, username = username,password = password,customer_info = newcustomer)
        try:
            newbankinfo.save()
        except IntegrityError:
            newcustomer.delete()
            user = {
                "response":"This username has been used already. Try another one."
            }
            return render(request,'createaccount.html',user)

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