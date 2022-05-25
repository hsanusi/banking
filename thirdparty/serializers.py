from rest_framework import serializers
from safemanager.models import Customer,Customer_Group

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        

class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Group
        fields = ('id','name','address','maximum_customer_allowed','logo','status')
