from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('BankingUI/', include('BankingUI.urls')),
    path('admin/', admin.site.urls),
]