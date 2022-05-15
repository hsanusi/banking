from django.contrib.auth.models import User
from .models import Customer

# Creating Customer Forms from the Customer Model
class CustomerForm():
    class Meta:
        model = Customer
        fields = [
            "title","surname","first_name","other_name","sex","date_of_birth","home_address","phone","email","status"
        ]