from django import forms
from django.contrib.auth.models import User
from testapp.models import Employee

class AddItemForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']

class EmployeeForm(forms.ModelForm):
     class Meta:
         model = Employee
         fields = '__all__'
