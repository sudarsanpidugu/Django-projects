from django.shortcuts import render
from django.http import HttpResponse
from .models import collegedata
# Create your views here.

def mainpage(request):
    rows = collegedata.objects.all()
    return render(request, 'mainpage.html',{'college1':rows})

def AddNewDetails(request):
    if request.method == 'GET':
        return render(request, 'collagedata.html')
    else:
        collegedata(
            first_name = request.POST.get('fname'),
            last_name = request.POST.get('lname'),
            email = request.POST.get('email'),
            mobile = request.POST.get('mobile'),
            college = request.POST.get('college'),
            branch = request.POST.get('brach'),
            percentage = request.POST.get('percentage'),
            location = request.POST.get('location'),
            fee = request.POST.get('fee'),
            ).save()
        rows = collegedata.objects.all()
        return render(request, 'mainpage.html',{'college1':rows})
    
        