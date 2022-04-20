from django.shortcuts import render
from django.http import HttpResponse

# from BankingUI.models import Customer,BankInfo,Transactions


def savenewaccountinfo(request):
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
            return HttpResponse(confirmpassword + password)
        newcustomer = Customer(
            first_name=firstname, last_name=lastname, birthday=birthday, email=email
        )
        newcustomer.save()
        newbankinfo = BankInfo(
            pin_number=pinnumber, username=username, password=password
        )
        if newbankinfo == newbankinfo:
            return HttpResponse(newbankinfo)
        # newbankinfo.save()
