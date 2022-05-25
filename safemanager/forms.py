from dataclasses import fields
from .models import Customer,Customer_Group
from django import forms


# Creating Customer Forms from the Customer Model
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "title",
            "surname",
            "first_name",
            "other_name",
            "sex",
            "date_of_birth",
            "marital_status",
             "passport",
            "home_address",
            "phone",
            "email",
            "occupation",
            "office_address",
            "next_of_kin",
            "next_of_kin_phone",
            "registered_by",
            "status"
        ]

class CustomerGroupForm(forms.ModelForm):
    class Meta:
        model = Customer_Group
        fields = '__all__'

