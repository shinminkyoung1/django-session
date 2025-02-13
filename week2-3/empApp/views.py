from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def employeeData(request):
    employees = Employee.objects.all()  # select * from empapp_employee
    empDict = {'employees': employees}
    return render(request, 'employees.html', empDict)