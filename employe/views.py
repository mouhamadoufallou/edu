from django.shortcuts import render, redirect  
from .forms import EmployeeForm  
from .models import Employee  

# Create your views here.  
def add_employe(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'employes/add_employe.html',{'form':form})  

def show_employes(request):  
    employees = Employee.objects.all()  
    return render(request,"employes/show_employes.html",{'employees':employees})  

def edit_employe(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'employes/edit_employe.html', {'employee':employee})  

def update_employe(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'employes/edit_employe.html', {'employee': employee})  

def destroy_employe(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")  