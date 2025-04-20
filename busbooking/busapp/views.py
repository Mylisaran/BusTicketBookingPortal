from django.shortcuts import render,redirect
from busapp.models import customer,booking_history,bus
from datetime import date
import random
# Create your views here.
def clean_up_history():
    today=date.today()
    booking=booking_history.objects.filter(travelling_date__lt=today)
    for i in booking:
        delete_booking=i.service_no
        delete_booking.seats_available+=i.no_of_seats
        delete_booking.save()
    booking.delete()

def login(request):
    clean_up_history()
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def bookbus(request):
    service_no=request.GET.get('service_no')
    price=request.GET.get('price')
    today=str(date.today())
    return render(request,'booking.html',{'service_no':service_no,'price':price,'today':today})

def cancelbus(request):
    return render(request,'cancel.html')

def create(request):
    name=request.POST.get('name')
    phno=request.POST.get('phno')
    password=request.POST.get('password')
    c_password=request.POST.get('c_pass')
    if password==c_password:
        a=customer(
        cname=name,
        phno=phno,
        password=password
        )
        a.save()
        return redirect('/')
    else:
        return redirect('signup')
    
def verify(request):
    name=request.POST.get('u_n')
    password=request.POST.get('password')
    a=customer.objects.filter(cname=name)
    if a[0].password==password:
        request.session['n']=name
        details=bus.objects.all()
        return render(request,'home.html',{'bus_details':details})
    else:
        return redirect('/')

def conform(request):                                       
    seats=request.GET.get('no_of_seats')
    service_no=request.GET.get('service_no')
    price=request.GET.get('price')
    travelling_date=request.GET.get('travelling_date')
    amount=int(seats)*int(price)
    customer_name=request.session['n']
    a=bus.objects.filter(service_no=service_no)
    start=a[0].start
    end=a[0].end
    cid=customer.objects.filter(cname=customer_name)[0].cid
    customer_instance=customer.objects.get(cid=cid)
    bus_instance=bus.objects.get(service_no=service_no)
    t_no=f'qwsed{random.randint(1000,9999)}'
    a=booking_history(
        ticket_no=t_no,
        customer_id=customer_instance,
        service_no=bus_instance,
        no_of_seats=seats,
        amount=amount,
        travelling_date=travelling_date
    )
    a.save()

    b=bus.objects.filter(service_no=service_no)[0]
    if b.seats_available>=int(seats):
        b.seats_available -=int(seats)
        b.save()
        return render(request,'ticket.html',{'seats':seats,'service_no':service_no,'amount':amount,'c_n':customer_name,'start':start,'end':end,'t_no':t_no,'date':travelling_date})
    else:
        return redirect('bookbus',{'error'f'AVAILABLE SEATS ARE {b.seats_available}.PLEASE CHOOSE ANOTHER SERVICE'})
