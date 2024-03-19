from django.shortcuts import render
from django.http import HttpResponse
from .models import studentdata
# Create your views here.

def mainpage(request):
    rows = studentdata.objects.all()
    return render(request, 'mainpage.html', {'student':rows})

def studentview(request):
    if request.method == 'GET':
        return render(request, 'studentdata.html')

    else:
        studentdata(
            first_name = request.POST.get('fname'),
            last_name = request.POST.get('lname'),
            email = request.POST.get('email'),
            mobile = request.POST.get('mobile'),
            course_name = request.POST.get('cname'),
            fee = request.POST.get('fee'),
            institute_name = request.POST.get('institute'),
            hometown = request.POST.get('hometown'),
            qulification = request.POST.get('qulification'),
            percentage = request.POST.get('percentage'),
        ).save()
        rows = studentdata.objects.all()
        return render(request, 'mainpage.html', {'student':rows})

def data(request, id):
    rows = studentdata.objects.get(id = id)
    return render(request, 'data.html',{'student':rows})

