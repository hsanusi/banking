from django.urls import path
from . import views

urlpatterns = [
    path('customer/register/',views.createCustomer,name="register_customer"),
    path('customer/customers/',views.getCustomers,name="customer_list"),
    path('customer/<str:pk>',views.updateCustomer,name="customer_details")
]