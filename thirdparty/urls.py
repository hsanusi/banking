from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('customers/',views.getCustomers),
    path('customers/<str:pk>',views.getCustomer),
    path('create_customer/',views.createCustomer),
    path('home',views.CustomerView.as_view())
]