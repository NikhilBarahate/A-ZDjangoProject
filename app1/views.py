from django.shortcuts import redirect, render
from app1.models import Employee
from app1.forms import EmployeeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def employeeView(request):
    form = EmployeeForm()
    template_name = "app1/employee.html"
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showemp_urls')
    
    context = {'form':form}
    return render(request, template_name, context)

@login_required()
def showEmployeeView(request):
    data = Employee.objects.all()
    template_name = "app1/showemp.html"
    context = {'data':data}
    return render(request, template_name, context)


def deleteView(request, id):
    data = Employee.objects.get(eid=id)
    template_name = "app1/confirm.html"
    if request.method == "POST":
        data.delete()
        return redirect('showemp_urls')

    context = {"data": data}
    return render(request, template_name, context)


def updateView(request, id):
    data = Employee.objects.get(eid=id)
    form = EmployeeForm(instance=data)
    template_name = "app1/employee.html"
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('showemp_urls')
    
    context = {'form':form}
    return render(request, template_name, context)




