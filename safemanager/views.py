from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import Customer

# This method is for registering new customers and maps to the url "customer/register/
def createCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid(): 
           form.save()
           return redirect('customer_list')
    else:
        logged_user = request.user
        context = {
            'registered_by': logged_user
            }
        form = CustomerForm(initial=context)
    context = {
        "form": form
    }
    return render(request,'safemanager/create_customer.html',context)

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

@login_required
def my_view(request):
    return HttpResponse(request.user.id)

@login_required(login_url='login')
def getCustomers(request):
    obj = Customer.objects.all()
    context = {
        "customers" : obj
    }
    return render(request, 'safemanager/customer_list.html', context)


def getCustomer(request,pk: int):
    obj = Customer.objects.get(id=pk)
    if obj is not None:
        context = {
            "customer" : obj
        }
        return render(request, 'safemanager/customer_detail.html', context)
    else:
        raise Http404('Customer does not exist')

def updateCustomer(request,pk: int):
    obj = Customer.objects.all().get(id=pk)
    form = CustomerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
    'form': form
    }
    return render(request,'safemanager/create_customer.html',context)


