from django.shortcuts import render
from django.http import HttpResponse
from .models import studentdata
# Create your views here.
def studentdataview(request):
    if request.method == 'GET':
        return render(request, 'studentdata.html')
    else:
        studentdata(
            first_name = request.POST.get('fname'),
            last_name = request.POST.get('lname'),
            email = request.POST.get('email'),
            mobile = request.POST.get('mobile'),
            college = request.POST.get('college'),
            qulification = request.POST.get('qulification'),
            branch = request.POST.get('brach'),
            percentage = request.POST.get('percentage'),
            fee = request.POST.get('fee'),
            ).save()
        return render(request, 'fetching.html')
        
def fetching_data(request):
    rows = studentdata.objects.all()
    return render(request, 'fetching.html', {'student':rows})