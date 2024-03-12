from django.shortcuts import render
from django.http import HttpResponse
from .models import contactform
# Create your views here.

def contactformview(request):
    if request.method == 'GET':
        return render(request, 'contactform.html')
    
    else:
        contactform(
            first_name = request.POST.get('fname'),
            last_name = request.POST.get('lname'),
            email = request.POST.get('email'),
            mobile = request.POST.get('mobile'),
            company = request.POST.get('company'),
            salary = request.POST.get('salary'),
            location = request.POST.get('location'),
        ).save()
        return render(request, 'contactform.html')