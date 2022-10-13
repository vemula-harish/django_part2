from django.shortcuts import render, redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm

# Create your views here.
def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request, 'index.html', {"emp_list":emp_list} )

def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'insert.html', {'form':form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance = employee)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, 'update.html', {'form':form})
