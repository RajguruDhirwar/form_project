import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SCP.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
faker=Faker()

def populate(n):
    for i in range(n):
        feno = randint(1010,9999)
        fename = faker.name()
        fesal = randint(10000,200000)
        feaddr = faker.city()
        emp_record = Employee.objects.get_or_create(
           eno = feno,
           ename = fename,
           esal = fesal,
           eaddr = feaddr
           )
n = int(input('Enter Number of Records:'))
populate(n)
print(f'{n} Records Inserted Succesfully')
