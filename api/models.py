from django.db import models

# Create your models here.
class Wallet(models.Model):
    # TABLE ROWS
    balance = models.DecimalField(max_digits=19, decimal_places=2)
    reward_point = models.IntegerField()
    cashback = models.IntegerField()
    limit_transaction = models.IntegerField()
    is_activate = models.BooleanField(max_length=15) #boolean value

class Total_History(models.Model):
    date = models.DateField()
    trans_mode = models.CharField(max_length=100)
    merchant = models.CharField(max_length=100)

class Newcard(models.Model):
    # TABLE ROWS
    charge = models.IntegerField()
    card_image = models.FileField() #image only one
    address = models.TextField()


class Library(models.Model):
    # TABLE ROWS
    book = models.CharField(max_length=150)
    history = models.ForeignKey("Total_History", on_delete=models.CASCADE)
    fine = models.IntegerField()
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE) #fogn ky
    date = models.DateField(max_length=150)
    time = models.TimeField(max_length=150)

class Cart(models.Model):
    book_no = models.CharField(max_length=150)
    book_name = models.CharField(max_length=150)
    available_card = models.CharField(max_length=150)


class Store(models.Model):
    # TABLE ROWS
    history = models.ForeignKey("Total_History", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField(max_length=15)
    time = models.TimeField(max_length=15)

class Canteen(models.Model):
    # TABLE ROWS
    history = models.ForeignKey("Total_History", on_delete=models.CASCADE)
    notification = models.CharField(max_length=300)


class Bus(models.Model):
    # TABLE ROWS
    history = models.ForeignKey("Total_History", on_delete=models.CASCADE)

class Fees(models.Model):
    # TABLE ROWS
    history = models.ForeignKey("Total_History", on_delete=models.CASCADE)
    fees_type = models.ForeignKey("Fee_type", on_delete=models.CASCADE) #foreign key

class Fee_type(models.Model):
    admission_fee = models.DecimalField(max_digits=19, decimal_places=2)
    waiver_scheme = models.DecimalField(max_digits=19, decimal_places=2)
    tution_spfee = models.DecimalField(max_digits=19, decimal_places=2)

class Events(models.Model):
    # TABLE ROWS
    event_name = models.CharField(max_length=100)
    event_logo = models.ImageField(null=True,default='')
    events_details = models.CharField(max_length=500)
    events_link = models.CharField(max_length=100)

class Paylater(models.Model):
    # TABLE ROWS
    limit = models.DecimalField(max_digits=19, decimal_places=2)
    spend = models.DecimalField(max_digits=19, decimal_places=2)
    offers = models.CharField(max_length=100)
    passbook = models.CharField(max_length=100)

class Settings(models.Model):
    # TABLE ROWS
    Terms_condition = models.CharField(max_length=100) #foreign key
    update = models.CharField(max_length=100) #foreign key
    help_support = models.CharField(max_length=100) #foreign key
    feedback = models.CharField(max_length=100)
    dispute = models.CharField(max_length=100)

class Profile(models.Model):
    # TABLE ROWS
    pic = models.ImageField()
    username = models.CharField(max_length=100) 
    password = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    passout = models.CharField(max_length=100)
    id_card = models.FileField() #document
    dob = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    nominee_name = models.CharField(max_length=100)
    nominee_dob = models.CharField(max_length=100)
    nominee_relation = models.CharField(max_length=100)
    nominee_address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)



class Others(models.Model):
    # TABLE ROWS
    igoal = models.ForeignKey("Igoal", on_delete=models.CASCADE) #foreign key
    invite_earn = models.CharField(max_length=100) #foreign key
    version = models.CharField(max_length=100) #foreign key
    company_profile = models.ImageField(max_length=100)
    company_name = models.CharField(max_length=100,default='')

class Igoal(models.Model):
    goal = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    tenure = models.CharField(max_length=100)
