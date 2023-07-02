from django.shortcuts import render
from .models import Employee


def index(request):
    employees = Employee.objects.all()
    # print("qyery: ", employees)

    employees = [i for i in employees]

    # print("Employees:", employees)

    # return employees list that shoul remove from iteration
    def clear_employers():
        parent_id_list = [i.parent_id for i in employees]  # [None, 1087, 1087]
        id_list = [i.id for i in employees]  # [1087, 1088, 1089]
        parent_id_equil_id = [id for id in  parent_id_list if id in id_list] # [1087, 1087]

        clear_workers = [] # workers that should remove for unrepeating in iteration in template
        for i, worker in enumerate(employees):
            # print(i, " | ", worker, " | ", worker.parent_id)

            if worker.parent_id in parent_id_equil_id:
                clear_workers.append(worker)
                #print("worker to remove:", worker.name)
        #print("clear_workers ****", clear_workers)
        return clear_workers

    # function that compare two lists and return list of needed employees
    def compare(*args):
        employees_res = []
        for e in employees:
            if e not in clear_employers():
                employees_res.append(e)
        return employees_res

    employees = compare(employees, clear_employers())
    #print("Change Employees:", employees)

    return render(request, "page/index.html", {'employees': employees})


def search(request):
    query_string = request.GET.get('q') # get string of search of GET

    if query_string:
        results = Employee.objects.filter(name=query_string)
        print(results)

    else:
        results = Employee.objects.all()

    return render(request, 'page/search.html', {'results': results, 'query_string': query_string})