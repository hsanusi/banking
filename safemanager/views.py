from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import Customer

"""
    createCustomer method instantiates the customer form as defined in the CustomerForm
    and the Customer Model. Login is required to access this view
"""
@login_required(login_url='login')
def createCustomer(request,redirect_template):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('customer_list')
    else:
        form = CustomerForm()
    context = {
        "form": form
    }
    return render(request,'customer_list',context)

"""
    updateCustomer method instantiates the customer form, loads the record of the customer from the database
    table and updates the record
"""
@login_required(login_url='login')
def updateCustomer(request,pk: int):
    obj = Customer.objects.all().get(id=pk)
    form = CustomerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
    'form': form
    }
    return render(request,'customer_list',context)

@login_required(login_url='login')
def getCustomers(request):
    obj = Customer.objects.all()
    context = {
        "customers" : obj
    }
    return render(request, 'customer_list', context)


def getCustomers(request,pk: int):
    obj = Customer.objects.get(id=pk)
    context = {
        "customer" : obj
    }
    return render(request, 'customer_list', context)


