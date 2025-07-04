from django.shortcuts import render,redirect
from django.views import View
from .models import Employee
from .forms import Add_Employee_Form

# Create your views here.
class Home(View):
    def get(self,request):
        data = Employee.objects.all()
        return render(request,'home.html',{'emp_data':data})


class Add_Student(View):
    def get(self,request):
        emp_data = Add_Employee_Form
        return render(request,'Add_Student.html',{'form':emp_data})
    
    def post(self,request):
        emp_data=Add_Employee_Form(request.POST)
        if (emp_data.is_valid):
            emp_data.save()
            return redirect('/')
        else:
            return render(request,'Add_Student.html',{'form':emp_data})

class Delete_Student(View):
    def post(self,request):
        data = request.POST
        emp_id=data.get('id')
        delete_record =  Employee.objects.get(id=emp_id)
        delete_record.delete()
        return redirect('/')
    
class Update_Record(View):
    def get(self,request,id):
        student=Employee.objects.get(id=id)
        form=Add_Employee_Form(instance=student)
        return render(request,'UpdateRecord.html',{'form':form})
    
    def post(self,request,id):

            data=Employee.objects.get(id=id)
            emp_data = Add_Employee_Form(request.POST, instance= data)
            if emp_data.is_valid():
                emp_data.save()
                return redirect('/')


    
    
