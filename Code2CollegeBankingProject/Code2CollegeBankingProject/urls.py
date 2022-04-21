from django.contrib import admin
from django.urls import include, path
from BankingUI import views
urlpatterns = [
    path('BankingUI/', include('BankingUI.urls')),
    path('admin/', admin.site.urls),
    path('BankingUI/createaccount',views.createaccount, name='createaccount'),
    path('BankingUI/forgotpassword',views.forgotpassword, name='forgotpassword'),
    path('BankingUI/index',views.index, name='index'),
    path('BankingUI/changeaccountinfo',views.changeaccountinfo, name='changeaccountinfo'),
    path('BankingUI/account',views.account, name='account'),
    path('BankingUI/changemoney',views.changemoney, name='changemoney'),
    path('BankingUI/todo',views.todo, name='todo'),
]