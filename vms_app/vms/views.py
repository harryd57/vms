from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Employees, Visitors

# Create your views here.


def home(request):
    return render(request, 'home.html')


def employee_signin(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        c_role = request.POST['c_role']

        p = Employees(first_name=fname,  last_name=lname,  email=email,
                      phone=phone, address=address, city=city, company_role=c_role)
        p.save()
        return redirect('home')
    else:
        return render(request, 'employee.html')


def visitor_signin(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        reason = request.POST['reason']

        p = Visitors(first_name=fname,  last_name=lname,  email=email,
                     phone=phone, address=address, city=city, reason=reason)
        p.save()
        return redirect('home')
    else:
        return render(request, 'visitor.html')


def employees(request):
    rows = Employees.objects.all()
    context = {
        'rows': rows
    }
    return render(request, 'employees.html', context)


def visitors(request):
    rows = Visitors.objects.all()
    context = {
        'rows': rows
    }
    return render(request, 'visitors.html', context)


def register(request):
    user = User.objects.values('is_staff')
    val = ''
    for i in user:
        val = i['is_staff']
    if val == False:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password']
            password2 = request.POST['password_confirm']

            if password1 == password2:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Password Not the same')
                return redirect('register')
        else:
            return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')


def base(request):
    return redirect('register')
