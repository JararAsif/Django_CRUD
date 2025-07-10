from django import forms
from .models import Employee

class Add_Employee_Form(forms.ModelForm):

    class Meta:
        model =  Employee
        fields= ("First_Name","Last_Name",'department_name')
        widgets ={
            'First_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Last_Name': forms.TextInput(attrs={'class':'form-control'}),
            'department_name':forms.TextInput(attrs={'class':'form-control'}),
        }

