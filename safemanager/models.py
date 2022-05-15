from django.db import models

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
    def _get_customer_id(self):
        custom = "00000" + self.id 
        return custom
    customer_id = property(_get_customer_id)
    group = models.ForeignKey(Customer_Group, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=6, choices=SHORT_TITLE)
    surname = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    other_name = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CODE)
    date_of_birth = models.DateField()
    home_address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50,null=True)
    status = models.BooleanField(default=True)
    next_of_kin = models.CharField(max_length=50, null=True)
    next_of_kin_phone = models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.surname
