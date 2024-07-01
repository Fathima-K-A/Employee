from django import forms
from EMP_CRM.models import Empmodel


class Employeeform(forms.Form):
     
     emp_name=forms.CharField(max_length=100)
     emp_place=forms.CharField(max_length=100)
     emp_age=forms.CharField(max_length=100)
     emp_position=forms.CharField(max_length=100)
    
    
class Empmodelform(forms.ModelForm):
     class Meta:
          model=Empmodel
          fields="__all__"      # for all fields
          # fields=['emp_name','emp_age','emp_position']
          # exclude=('emp_place',)