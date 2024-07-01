from django.shortcuts import render
from django.views.generic import View
from EMP_CRM.forms import Employeeform,Empmodelform
from EMP_CRM.models import Empmodel

class Register(View):
    
    def get(self,request):
        
        form=Employeeform()
        
        return render(request,"index.html",{"form":form})
    
    
    def post(self,request):
        
        form=Employeeform(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("emp_name"))
            # ORM == object relational mapping
            # Empmodel.objects.create(**form.cleaned_data)
            name=form.cleaned_data.get("emp_name")
            place=form.cleaned_data.get("emp_place")
            age=form.cleaned_data.get("emp_age")
            position=form.cleaned_data.get("emp_position")
            Empmodel.objects.create(emp_name=name,emp_place=place,emp_age=age,emp_position=position)
            return render(request,"index.html")
        else:
            return render(request,"index.html")
        
        
# using model form for create
class Empmodelview(View):
    def get(self,request):
        form=Empmodelform()
        return render(request,"index2.html",{"form":form})
    
    def post(self,request):
        form=Empmodelform(request.POST)
        if form.is_valid():
            form.save()     # create    update 
        return render(request,"index2.html") 
    

# read

class Employees(View):
    
    def get(self,request):
        
        data=Empmodel.objects.all()
        # to get all the objects from table
        
        return render(request,"index3.html",{"data":data})


# to get the data of a unique object using id
class Employeedetail(View):
    def get(self,request,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        data=Empmodel.objects.get(id=id)
        return render(request,"index4.html",{"data":data})
    
    

# delete   

class Employeedelete(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        Empmodel.objects.get(id=id).delete()
        print("deleted successfully")
        return render(request,"index.html")


# update

class EmpUpdate(View):
    
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Empmodel.objects.get(id=id)
        form=Empmodelform(instance=data)
        
        return render(request,"index5.html",{"form":form})
    
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=Empmodel.objects.get(id=id)
        form=Empmodelform(request.POST,instance=data)
        print(request.POST)
        if form.is_valid():
            form.save()      
            # save method can only used for create and update
            # if there is no ORM query then,
            # Empmodel.objects.create(**form.cleaned_data)    **is is used to unpack the key and value from the dictionary,convert it and add it to the table.
            print("updated successfully")
        form=Empmodelform()
        return render(request,"index5.html",{"form":form})