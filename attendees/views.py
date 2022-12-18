from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from attendees.form import EmpForm

def attendees_reg(request):
    stu = EmpForm()
    return render(request, "attendees_reg.html",{'form':stu})


    