from django.shortcuts import render
from django.http import HttpResponse
from .models import employeeformdata

# Create your views here.
def employeesformview(request):
    if request.method == 'GET':
        return render(request, 'employee.html')
    else:
        employeeformdata(
            first_name = request.POST.get('fname'),
            last_name = request.POST.get('lname'),
            email = request.POST.get('email'),
            mobile = request.POST.get('mobile'),
            qulification = request.POST.get('qulification'),
            branch = request.POST.get('brach'),
            percentage = request.POST.get('percentage'),
            passed_out_year = request.POST.get('year'),
            skills = request.POST.get('skills'),
        ).save()
        return render(request, 'employee.html')
