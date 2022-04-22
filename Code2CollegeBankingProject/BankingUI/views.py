from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        pin_number = request.POST["password"]
        try:
            customerbankinfo = User.objects.get(username=username)
            # return HttpResponse(customerbankinfo.customer_info.first_name)
            if User.check_password(pin_number) == True:
                user = {
                    "name":User.get_full_name(),
                    "email":User.email
                    # query the transactions and then find everything inside
                }
                request.session['userid'] = User.id #use this to reference user stuff
                return render(request,'account.html',user)#password and user is for the same user
            else:
                user = {
                "response":"Your username or password was incorrect. Try again. Click here to change your password."
            }
                return render(request,'index.html',user)
        except ObjectDoesNotExist:
            user = {
                "response":"Your username or password was incorrect. Try again. Click here to change your password."
            }
            return render(request,'index.html',user)
    return render(request,'index.html')

def createaccount(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        pinnumber = request.POST["pinnumber"]
        # check if user/email is unique then create user
        try:
            newcustomer = User.objects.create_user(username, email, pinnumber)
            newcustomer.first_name = first_name
            newcustomer.last_name = last_name
            newcustomer.save()
        except IntegrityError:
            newcustomer.delete()
            user = {
                "response":"This username/email has been used already. Try another one."
            }
            return render(request,'createaccount.html',user)

    return render(request,'createaccount.html')

def forgotpassword(request):
    userid = request.session['userid']
    customerbankinfo = User.objects.get(id = userid)
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        pin_number = request.POST["pin_number"]
        if customerbankinfo.check_password(pin_number) == True:
            user = {
                "response":"Your new password does not match the confirming password"
            }
            render(request,'forgotpassword.html',user)
        try:
            customerbankinfo = User.objects.get(username = username)
            if first_name == customerbankinfo.first_name and last_name == customerbankinfo.last_name and email == customerbankinfo.email and customerbankinfo.pin_number == str(customerbankinfo.pin_number):
                customerbankinfo.pin_number = pin_number
                customerbankinfo.save()
                user = {
                    "response":"Password was saved"
                }
                return render(request,'forgotpassword.html',user)

            else:
                user = {
                    "response":"One or more of your fields are incorrect"
                }
                # return HttpResponse(f'{birthday == str(customerbankinfo.customer_info.birthday)}')
                # return HttpResponse(f'{firstname == customerbankinfo.customer_info.first_name}, {lastname == customerbankinfo.customer_info.last_name} ,{birthday == str(customerbankinfo.customer_info.birthday)}, {email == customerbankinfo.customer_info.email}, {pin_number == str(customerbankinfo.pin_number)}')

                return render(request,'forgotpassword.html',user)
        except ObjectDoesNotExist:
            user = {
                "response":"This username doesn't exist"
            }
            return render(request,'forgotpassword.html',user)
    return render(request,'forgotpassword.html')

def account(request):
    userid = request.session['userid']
    customerbankinfo = User.objects.get(id = userid)
    user = {
    "firstname":User.first_name,
    "lastname":User.last_name,
    "email":User.email
    }
    return render(request,'account.html', user)

def changeaccountinfo(request):
    return render(request,'changeaccountinfo.html')

def changemoney(request):
    userid = request.session['userid']
    customerbankinfo = User.objects.get(id = userid)
    if request.method == "POST":
        transactiontype = request.POST.get('transactiontype')
        amount = request.POST.get('amount')
        newtransaction = Transactions(transactiontype = transactiontype, amount = amount, account = customerbankinfo)
        newtransaction.save()
    return render(request,'changemoney.html')

# add required field into the end of html forms after testing

def todo(request):
    return render(request,'todo.html')