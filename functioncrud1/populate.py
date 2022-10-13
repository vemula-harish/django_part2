import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','functioncrud1.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
from random import *
faker = Faker()

def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fename = faker.name()
        fesal = randint(10000,20000)
        feadd = faker.city()
        emp_record = Employee.objects.get_or_create(
                        eno = feno,
                        ename = fename,
                        esal = fesal,
                        eadd = feadd
        )
n = int(input("enter no of records:"))
populate(n)
print(f'{n} Records Inserted Successfully')
