from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,BankInfo,Transactions
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            customerbankinfo = BankInfo.objects.get(username=username)
            # return HttpResponse(customerbankinfo.customer_info.first_name)
            if password == customerbankinfo.password:
                user = {
                    "firstname":customerbankinfo.customer_info.first_name,
                    "lastname":customerbankinfo.customer_info.last_name,
                    "email":customerbankinfo.customer_info.email
                    # query the transactions and then find everything inside
                }
                request.session['userid'] = customerbankinfo.id #use this to reference user stuff
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
                "response":"Your new password does not match the confirming password"
            }
            render(request,'forgotpassword.html',user)
        try:
            customerbankinfo = BankInfo.objects.get(username = username)
            if firstname == customerbankinfo.customer_info.first_name and lastname == customerbankinfo.customer_info.last_name and birthday == str(customerbankinfo.customer_info.birthday) and email == customerbankinfo.customer_info.email and pinnumber == str(customerbankinfo.pin_number):
                customerbankinfo.password = password
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
                # return HttpResponse(f'{firstname == customerbankinfo.customer_info.first_name}, {lastname == customerbankinfo.customer_info.last_name} ,{birthday == str(customerbankinfo.customer_info.birthday)}, {email == customerbankinfo.customer_info.email}, {pinnumber == str(customerbankinfo.pin_number)}')

                return render(request,'forgotpassword.html',user)
        except ObjectDoesNotExist:
            user = {
                "response":"This username doesn't exist"
            }
            return render(request,'forgotpassword.html',user)
    return render(request,'forgotpassword.html')

def account(request):
    userid = request.session['userid']
    customerbankinfo = BankInfo.objects.get(id = userid)
    user = {
    "firstname":customerbankinfo.customer_info.first_name,
    "lastname":customerbankinfo.customer_info.last_name,
    "email":customerbankinfo.customer_info.email
    }
    return render(request,'account.html', user)

def changeaccountinfo(request):
    return render(request,'changeaccountinfo.html')

def changemoney(request):
    userid = request.session['userid']
    customerbankinfo = BankInfo.objects.get(id = userid)
    if request.method == "POST":
        transactiontype = request.POST.get('transactiontype')
        amount = request.POST.get('amount')
        newtransaction = Transactions(transactiontype = transactiontype, amount = amount, account = customerbankinfo)
        newtransaction.save()
    return render(request,'changemoney.html')

# add required field into the end of html forms after testing

def todo(request):
    return render(request,'todo.html')

# this is a test