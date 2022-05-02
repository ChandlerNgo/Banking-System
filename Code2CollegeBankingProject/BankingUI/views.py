from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Transactions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        pin_number = request.POST["pinnumber"]
        user = authenticate(request, username=username, password=pin_number)
        if user is not None:  # user exists
            login(request, user)
            # customer_transactions = Transactions.objects.filter(account = user.id)
            # customer_amount = 0
            # for transactions in customer_transactions:
            #     if transactions.transactiontype == "Deposit":
            #         customer_amount = customer_amount + transactions.amount
            #     if transactions.transactiontype == "Withdraw":
            #         customer_amount = customer_amount - transactions.amount
            # userinfo = {
            # "firstname":user.first_name,
            # "lastname":user.last_name,
            # "email":user.email,
            # "money": customer_amount,
            # "transactions": customer_transactions
            # }
            return redirect(account)
            # return redirect(request,'account.html',userinfo)
        else:
            userinfo = {"response": "Your login information is incorrect"}
            return render(request,"index.html",userinfo)
    return render(request,"index.html")


def createaccount(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        pinnumber = request.POST["pinnumber"]
        # check if user/email is unique then create user
        if User.objects.filter(email=email).exists():
            userinfo = {"response": "This email has been used already"}
            return render(request, "createaccount.html", userinfo)
        elif User.objects.filter(username=username).exists():
            userinfo = {"response": "This username has been used already"}
            return render(request, "createaccount.html", userinfo)
        else:
            newcustomer = User.objects.create_user(
                username=username, email=email, password=pinnumber
            )
            newcustomer.first_name = first_name
            newcustomer.last_name = last_name
            newcustomer.save()
            userinfo = {"response": "Your bank account has been created"}
        return render(request, "createaccount.html", userinfo)
    return render(request,"createaccount.html")


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

        if User.objects.filter(username=username).exists():
            customer_bank_info = User.objects.get(username=username)
            if (
                customer_bank_info.first_name == first_name
                and customer_bank_info.last_name == last_name
                and customer_bank_info.email == email
            ):  # personal info is correct
                is_password_correct = check_password(
                    pin_number, customer_bank_info.password
                )
                if is_password_correct:  # password is correct
                    if pin_number != new_pin_number:
                        customer_bank_info.set_password(new_pin_number)
                        customer_bank_info.save()
                        userinfo = {"response": "Your pin has been changed"}
                        return render(request, "forgotpassword.html", userinfo)
                    else:
                        userinfo = {
                            "response": "Your pin number is the same as the new password"
                        }
                        return render(request, "forgotpassword.html", userinfo)
                else:
                    userinfo = {"response": "One of your fields is not correct"}
                    return render(request, "forgotpassword.html", userinfo)
            else:
                userinfo = {"response": "One of your fields is not correct"}
                return render(request, "forgotpassword.html", userinfo)
        else:
            userinfo = {"response": "This username doesn't exist"}
            return render(request, "forgotpassword.html", userinfo)
    return render(request,"forgotpassword.html")


@login_required(login_url='/BankingUI/index')
def account(request):
    customer_transactions = Transactions.objects.filter(account=request.user.id)
    balance = 0

    for transaction in customer_transactions:
        transaction.balance = balance
        if transaction.transactiontype == "Deposit":
            balance += transaction.amount
        if transaction.transactiontype == "Withdraw":
            balance -= transaction.amount
        transaction.balance = balance
        
    userinfo = {
        "firstname": request.user.first_name,
        "lastname": request.user.last_name,
        "email": request.user.email,
        "money": balance,
        "transactions": customer_transactions,
    }
    return render(request,"account.html", userinfo)


@login_required(login_url='/BankingUI/index')
def changeaccountinfo(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        if (
            not User.objects.filter(username=username).exists()
            or request.user.username == username
        ):  # if the username doensn't exist
            if (
                not User.objects.filter(email=email).exists()
                or request.user.email == email
            ):  # if the email doensn't exist
                request.user.first_name = first_name
                request.user.last_name = last_name
                request.user.email = email
                request.user.username = username
                request.user.save()
                userinfo = {
                    "title": request.user.first_name,
                    "response": "Your new information has been saved",
                }
                return render(request,"changeaccountinfo.html", userinfo)
            else:
                userinfo = {
                    "title": request.user.first_name,
                    "response": "The email is already in use",
                }
                return render(request,"changeaccountinfo.html", userinfo)
        else:
            userinfo = {
                "title": request.user.first_name,
                "response": "The username is already in use",
            }
            return render(request,"changeaccountinfo.html", userinfo)
    userinfo = {
        "title": request.user.first_name
    }
    return render(request,"changeaccountinfo.html", userinfo)


@login_required(login_url='/BankingUI/index')
def changemoney(request):
    if request.method == "POST":
        transaction_type = request.POST.get("transactiontype")
        amount = request.POST.get("amount")
        customer_transactions = Transactions.objects.filter(
            account=request.user.id
        )  # user is not recognized
        customer_amount = 0
        for transaction in customer_transactions:
            if transaction.transactiontype == "Deposit":
                customer_amount += transaction.amount
            if transaction.transactiontype == "Withdraw":
                customer_amount -= transaction.amount
        if transaction_type == "Withdraw" and customer_amount - int(amount) < 0:
            userinfo = {"response": "You do not have enough money in your account"}
            return render(request, "changemoney.html", userinfo)
        newtransaction = Transactions(
            transactiontype=transaction_type, amount=amount, account=request.user
        )
        newtransaction.save()
        userinfo = {"response": "Your transaction has been made"}
        return render(request, "changemoney.html", userinfo)
    return render(request,"changemoney.html")
# https://stackoverflow.com/questions/39560175/redirect-to-same-page-after-post-method-using-class-based-views

# add required field into the end of html forms after testing

@login_required(login_url='/BankingUI/index')
def deleteaccount(request):
    pin_number = request.POST.get("pinnumber")
    if request.method == "POST":
        if check_password(pin_number, request.user.password):
            userinfo = {
                "response": "Your account has been deleted.. along with all your money"
            }
            request.user.delete()
            return redirect(index, userinfo)
        else:
            userinfo = {"response": "Your pin number is not right"}
            return render(request, "deleteaccount.html", userinfo)
    return render(request,"deleteaccount.html")


def logout_view(request):
    logout(request)
    return redirect(index)
