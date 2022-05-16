from django.db import models
from django.contrib.auth.models import User

class Customer_Group(models.Model):
    name = models.CharField(max_length=150, null=False)
    address = models.TextField(max_length=50, null=False)
    maximum_customer_allowed = models.IntegerField()
    logo = models.CharField(max_length=50, null=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    SEX_CODE = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    SHORT_TITLE = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
        ('Engr', 'Engr'),
        ('Prof', 'Prof'),
        ('Elder', 'Elder'),
        ('Oba', 'Oba'),
    )

    MARITAL_STATUS = (
        ('Single', 'Single'),
        ('Maried', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widow', 'Widow'), 
    )
    
    customer_id = models.CharField(max_length=4,null=True)
    group = models.ForeignKey(Customer_Group, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=6, choices=SHORT_TITLE)
    surname = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    other_name = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CODE)
    date_of_birth = models.DateField()
    home_address = models.TextField()
    phone = models.CharField(max_length=15)
    occupation = models.CharField(max_length=50,null=True)
    office_address = models.TextField(null=True)
    email = models.EmailField(max_length=50,null=True)
    marital_status = models.CharField(max_length=15, choices=MARITAL_STATUS, default='Single')
    status = models.BooleanField(default=True)
    next_of_kin = models.CharField(max_length=50, null=True)
    next_of_kin_phone = models.CharField(max_length=50, null=True)
    registered_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    passport = models.ImageField(upload_to='images/', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.surname
