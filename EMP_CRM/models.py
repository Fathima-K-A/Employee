from django.db import models

class Empmodel(models.Model):
    
    emp_name=models.CharField(max_length=100,null=False)
    emp_place=models.CharField(max_length=100,null=True)
    emp_age=models.CharField(max_length=100,null=False)
    emp_position=models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return self.emp_name
    
