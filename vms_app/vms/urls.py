from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('employee_signin', views.employee_signin, name='employee_signin'),
    path('visitor_signin', views.visitor_signin, name='visitor_signin'),
    path('visitors', views.visitors, name='visitors'),
    path('employees', views.employees, name='employees'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login')
]
