from http.client import HTTPS_PORT
from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        pin_number = request.POST["pinnumber"]

        if User.objects.filter(username = username).exists():
            customer_bank_info = User.objects.get(username = username)
            is_password_correct = check_password(pin_number, customer_bank_info.password)
            if is_password_correct == True:

                # account(request)

                request.session['userid'] = customer_bank_info.id
                userid = request.session['userid'] = customer_bank_info.id
                customer_bank_info = User.objects.get(id = userid)
                customer_transactions = Transactions.objects.filter(account = customer_bank_info.id)
                customer_amount = 0
                date_transaction_type_amount = []
                for transactions in customer_transactions:
                    if transactions.transactiontype == "Deposit":
                        customer_amount = customer_amount + transactions.amount
                    if transactions.transactiontype == "Withdraw":
                        customer_amount = customer_amount - transactions.amount
                    date_transaction_type_amount.append(transactions)
                    # date_transaction_type_amount.append([transactions.date,transactions.transactiontype,transactions.amount])
                user = {
                "firstname":customer_bank_info.first_name,
                "lastname":customer_bank_info.last_name,
                "email":customer_bank_info.email,
                "money": customer_amount,
                "transactions": date_transaction_type_amount
                }
                return render(request,'account.html', user)

                # 

                
            else:
                user = {
                "response":"The password is not correct"
                }
                return render(request,'index.html',user)
        else:
            user = {
                "response":"This username doesn't exist"
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
        if User.objects.filter(email = email).exists() == True:
            user = {
                "response":"This email has been used already"
            }
            return render(request,'createaccount.html',user)
        elif User.objects.filter(username = username).exists() == True:
            user = {
                "response":"This username has been used already"
            }
            return render(request,'createaccount.html',user)
        else:
            newcustomer = User.objects.create_user(username = username, email = email, password = pinnumber)
            newcustomer.first_name = first_name
            newcustomer.last_name = last_name
            newcustomer.save()
            user = {
                "response":"Your bank account has been created"
            }
        return render(request,'createaccount.html',user)

        

    return render(request,'createaccount.html')

def forgotpassword(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        pin_number = request.POST["pinnumber"]
        new_pin_number = request.POST["newpinnumber"]
        # check if user exists
        # see if the other fields match
        # see if password matches
        # change the password

# should the person be able to change their pin with or without their old pin

        if User.objects.filter(username = username).exists():
            customer_bank_info = User.objects.get(username = username)
            if customer_bank_info.first_name == first_name and customer_bank_info.last_name == last_name and customer_bank_info.email == email:# personal info is correct
                is_password_correct = check_password(pin_number, customer_bank_info.password)
                if is_password_correct == True:#password is correct
                    if pin_number != new_pin_number:
                        customer_bank_info.set_password(new_pin_number)
                        customer_bank_info.save()
                        user = {
                            "response":"Your new pin number has been created"
                        }
                        return render(request, 'forgotpassword.html', user)
                    else:
                        user = {
                            "response":"Your pin number is the same as the new password"
                        }
                        return render(request, 'forgotpassword.html', user)
                else:
                    user = {
                            "response":"Your pin number is not correct"
                        }
                    return render(request, 'forgotpassword.html', user)
            else:
                user = {
                    "response":"One of your fields is not correct"
                }
                return render(request, 'forgotpassword.html', user)
        else:
            user = {
                    "response":"This username doesn't exist"
                }
            return render(request, 'forgotpassword.html', user)
    return render(request,'forgotpassword.html')

def account(request):
    userid = request.session['userid']
    customer_bank_info = User.objects.get(id = userid)
    customer_transactions = Transactions.objects.filter(account = customer_bank_info.id)
    customer_amount = 0
    date_transaction_type_amount = []
    for transactions in customer_transactions:
        if transactions.transactiontype == "Deposit":
            customer_amount = customer_amount + transactions.amount
        if transactions.transactiontype == "Withdraw":
            customer_amount = customer_amount - transactions.amount
        date_transaction_type_amount.append(transactions)
        # date_transaction_type_amount.append([transactions.date,transactions.transactiontype,transactions.amount])
    user = {
    "firstname":customer_bank_info.first_name,
    "lastname":customer_bank_info.last_name,
    "email":customer_bank_info.email,
    "money": customer_amount,
    "transactions": date_transaction_type_amount
    }
    return render(request,'account.html', user)

def changeaccountinfo(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]

        userid = request.session['userid']
        customer_bank_info = User.objects.get(id = userid)
        if User.objects.filter(username = username).exists() == False or customer_bank_info.username == username:#if the username doensn't exist
            if User.objects.filter(email = email).exists() == False or customer_bank_info.email == email:#if the email doensn't exist
                customer_bank_info.first_name = first_name
                customer_bank_info.last_name = last_name
                customer_bank_info.email = email
                customer_bank_info.username = username
                customer_bank_info.save()
                user = {
                    "response":"Your new information has been saved"
                }
                return render(request,'changeaccountinfo.html',user)
            else:
                user = {
                "response":"The email is already in use"
                }
                return render(request,'changeaccountinfo.html',user)
        else:
            user = {
            "response":"The username is already in use"
            }
            return render(request,'changeaccountinfo.html',user)
    return render(request,'changeaccountinfo.html')

def changemoney(request):
    userid = request.session['userid']
    customer_bank_info = User.objects.get(id = userid)
    if request.method == "POST":
        transaction_type = request.POST.get('transactiontype')
        amount = request.POST.get('amount')


        customer_transactions = Transactions.objects.filter(account = customer_bank_info.id)
        customer_amount = 0
        for transactions in customer_transactions:
            if transactions.transactiontype == "Deposit":
                customer_amount = customer_amount + transactions.amount
            if transactions.transactiontype == "Withdraw":
                customer_amount = customer_amount - transactions.amount
        if transaction_type == 'Withdraw' and customer_amount - int(amount) < 0:
            user = {
                    "response":"You do not have enough money in your account"
                }
            return render(request, 'changemoney.html', user)
        newtransaction = Transactions(transactiontype = transaction_type, amount = amount, account = customer_bank_info)
        newtransaction.save()
        user = {
                    "response":"Your transaction has been made"
                }
        return render(request, 'changemoney.html', user)
    return render(request,'changemoney.html')

# add required field into the end of html forms after testing

def todo(request):
    return render(request,'todo.html')