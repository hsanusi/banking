from rest_framework import serializers
from safemanager.models import Customer,Customer_Group

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id',"title","surname","first_name","other_name","sex","date_of_birth","home_address","phone","status","date_joined")
        

class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Group
        fields = ('id','name','address','maximum_customer_allowed','logo','status')
