from django.urls import path
from . import views

urlpatterns = [
    path('customer/register/',views.createCustomer,name="register_customer"),
    path('customer/customers/',views.getCustomers,name="customer_list"),
    path('customer/<str:pk>',views.updateCustomer,name="customer_details"),
    path('group/register/',views.createCustomerGroup,name="register_group"),
    path('group/groups/',views.getGroups,name="group_list"),
    path('group/<str:pk>',views.updateGroup,name="customer_details"),
    path('test/template/',views.index),
]