from django.contrib import admin
# Register your models here.
from busapp.models import *
@admin.register(bus)
class bus(admin.ModelAdmin):
    list_display=['service_no','start','end','seats_available','price']
    search_fields=['service_no','price']

@admin.register(customer)
class customer(admin.ModelAdmin):
    list_display=['cid','cname','phno','password']
    search_fields=['cid']

@admin.register(booking_history)
class booking_history(admin.ModelAdmin):
    list_display=['ticket_no','customer_id','service_no','no_of_seats','amount']
    search_fields=['ticket_no']      