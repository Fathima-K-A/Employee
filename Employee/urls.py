"""Employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EMP_CRM.views import Register,Empmodelview,Employees,Employeedetail,Employeedelete,EmpUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',Register.as_view()),
    path('model/',Empmodelview.as_view()),
    path('all/',Employees.as_view()),
    path('all/<int:pk>',Employeedetail.as_view()),
    path("delete/<int:pk>",Employeedelete.as_view()),
    path("update/<int:pk>",EmpUpdate.as_view())
]
