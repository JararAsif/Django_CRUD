from django import forms
from .models import Employee

class Add_Employee_Form(forms.ModelForm):

    class Meta:
        model =  Employee
        fields= ("First_Name","Last_Name","Emp_id")
        widgets ={
            'First_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Last_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Emp_id': forms.NumberInput(attrs={'class':'form-control'}),
        }

