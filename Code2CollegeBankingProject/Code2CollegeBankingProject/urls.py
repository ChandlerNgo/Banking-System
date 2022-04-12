from django.contrib import admin
from django.urls import include, path
from BankingUI import views
urlpatterns = [
    path('BankingUI/', include('BankingUI.urls')),
    path('admin/', admin.site.urls),
    path('BankingUI/createaccount',views.createaccount, name='createaccount'),
    path('BankingUI/forgotpassword',views.forgotpassword, name='forgotpassword'),
    path('BankingUI/index',views.index, name='index')
]