from django.db import models
from django.utils import timezone

# Create your models here.
class customer(models.Model):
    cid=models.BigAutoField(primary_key=True)
    cname=models.CharField(max_length=200)
    phno=models.IntegerField()
    password=models.CharField(max_length=200)

class bus(models.Model):
    service_no=models.IntegerField(primary_key=True)
    start=models.CharField(max_length=100)
    end=models.CharField(max_length=100)
    seats_available=models.IntegerField()
    price=models.IntegerField()

class booking_history(models.Model):
    ticket_no=models.CharField(primary_key=True,max_length=200)
    customer_id=models.ForeignKey(customer,on_delete=models.RESTRICT)
    service_no=models.ForeignKey(bus,on_delete=models.RESTRICT)
    no_of_seats=models.IntegerField()
    amount=models.IntegerField()
    travelling_date=models.DateField(default=timezone.now)

