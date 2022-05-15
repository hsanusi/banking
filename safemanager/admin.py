from django.contrib import admin
from .models import Customer, Customer_Group

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("title","surname","first_name","other_name","sex","date_of_birth","home_address","phone","email","status","date_joined")

class CustomerGroupAdmin(admin.ModelAdmin):
    list_display = ('name','address','maximum_customer_allowed','logo','status')

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Customer_Group,CustomerGroupAdmin)