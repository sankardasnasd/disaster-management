from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class camp_table(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    capacity=models.BigIntegerField()
    details=models.CharField(max_length=100)
    lattitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)
    image=models.FileField()


class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone_number=models.BigIntegerField()


class coordinator_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    CAMP=models.ForeignKey(camp_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=30)
    phone_number=models.BigIntegerField()
    email=models.CharField(max_length=100)
    image=models.FileField()

class complaint_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    COORDINATOR=models.ForeignKey(coordinator_table,on_delete=models.CASCADE)
    CAMP=models.ForeignKey(camp_table,on_delete=models.CASCADE)
    complaints=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    date=models.DateField()

class volunteer_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image=models.FileField()
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)

class guideline_table(models.Model):
    COORDINATOR=models.ForeignKey(coordinator_table,on_delete=models.CASCADE)
    guidelines=models.FileField()
    details=models.CharField(max_length=100)
    date=models.DateField()

class notification(models.Model):
    notification=models.CharField(max_length=100)
    date=models.DateField()
    details=models.CharField(max_length=100)

class goods_table(models.Model):
    COORDINATOR=models.ForeignKey(coordinator_table,on_delete=models.CASCADE)
    type=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    date=models.DateField()
    details=models.CharField(max_length=100)
    stock=models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

class needs_table(models.Model):
    COORDINATOR=models.ForeignKey(coordinator_table,on_delete=models.CASCADE)
    GOODS=models.ForeignKey(goods_table,on_delete=models.CASCADE)
    date=models.DateField()
    quantity=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class donate_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    NEEDS=models.ForeignKey(needs_table,on_delete=models.CASCADE)
    date=models.DateField()
    quantity=models.CharField(max_length=100)

class services_table(models.Model):
    type=models.CharField(max_length=100)
    details=models.CharField(max_length=100)

class item_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    type=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    picture=models.FileField()
    status=models.CharField(max_length=100)

class medical_support_table(models.Model):
    COORDINATOR=models.ForeignKey(coordinator_table,on_delete=models.CASCADE)
    details=models.CharField(max_length=100)
    date=models.DateField()
    status=models.CharField(max_length=100)

class emergency_response_team_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    experience=models.CharField(max_length=100)

class request_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    EMERGENCY=models.ForeignKey(emergency_response_team_table,on_delete=models.CASCADE)
    details=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date=models.CharField(max_length=100)


class Complaint(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    complaints=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    date=models.DateField()