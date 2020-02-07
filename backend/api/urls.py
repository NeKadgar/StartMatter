from api import views
from django.urls import path

urlpatterns = [
    path('customers_around/', views.CustomersAround),
    #path('customers_around2/', views.CustomersAround2),
]
