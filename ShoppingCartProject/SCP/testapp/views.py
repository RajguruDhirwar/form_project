from django.shortcuts import render,redirect
from testapp.forms import AddItemForm
from django.contrib.auth.decorators import login_required
from testapp.forms import *
from django.http import HttpResponseRedirect
from testapp.models import Employee
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    return render(request,'testapp/home.html')

def additem_view(request):
    form = AddItemForm()
    response = render(request,'testapp/additem.html',{'form':form})
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']

            response.set_cookie(name,quantity)
    return response

def display_items_view(request):
    return render(request,'testapp/displayitem.html')

def index1_view(request):
    return render(request,'testapp/index1.html')

def home_page_view(request):
    return render (request, 'testapp/homeauth.html')

@login_required
def java_page_view(request):
    return render (request, 'testapp/java.html')

@login_required
def python_page_view(request):
    return render (request, 'testapp/python.html')

@login_required
def aptitude_page_view(request):
    return render (request, 'testapp/aptitude.html')


def logout_view(request):
    return render (request, 'testapp/logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render (request, 'testapp/signup.html',{'form':form})


def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request,'testapp/index2.html',{'emp_list':emp_list})

def insert_view(request):
    form = EmployeeForm()
    if request.method =='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/emp')
    return render(request,'testapp/insert.html',{'form':form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/emp')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance = employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/emp')
    return render(request,'testapp/update.html',{'form':form})


class HelloWorldView(View):
    def get(self,request):
        return HttpResponse()
