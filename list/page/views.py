from django.shortcuts import render
from .models import Employee


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    print("qyery: ", employees)

    employees = [i for i in employees]
    print("Employees:", employees)

    def clear_employers():
        parent_id_list = [i.parent_id for i in employees]                    # [None, 1087, 1087]
        id_list = [i.id for i in employees]                                  # [1087, 1088, 1089]
        parent_id_equil_id = [id for id in  parent_id_list if id in id_list] # [1087, 1087]

        clear_workers = [] # workers that should remove for unrepeating in iteration in template
        for i, worker in enumerate(employees):
            print(i, " | ", worker, " | ", worker.parent_id)

            if worker.parent_id in parent_id_equil_id:
                clear_workers.append(worker)
                print("worker to remove:", worker.name)
        print("clear_workers ****", clear_workers)
        return clear_workers

    # function that campare two lists and return list of needed employees
    def compare(*args):
        employees_res = []
        for e in employees:
            if e not in clear_employers():
                print(e)
                employees_res.append(e)
        return employees_res
    print("Change Employees:", employees)
    employees = compare(employees, clear_employers())
    print("Change Employees:", employees)

    return render(request, "page/index.html", {'employees': employees})