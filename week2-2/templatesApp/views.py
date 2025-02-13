from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict = {"name": "숭멋사"}
    return render(request, 'firstTemplate.html', context=myDict)

def renderEmployee(request):
    myDict = {"id": 123, "name": "숭멋사", "sal": 10000}
    return render(request, 'employeeTemplate.html', context=myDict)