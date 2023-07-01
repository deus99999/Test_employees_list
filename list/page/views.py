from django.shortcuts import render
from .models import Employee


# Create your views here.
def index(request):
    employees = Employee.objects.all()

    # l = []
    # for employee in employees:
    #     l.append(employee.get_hierarchy())
    # print(l)


    return render(request, "page/index.html", {'employees': employees})