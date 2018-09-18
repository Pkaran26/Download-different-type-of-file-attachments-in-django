from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=25)
    post = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    join_date = models.DateField(auto_now_add=True)
    salary = models.CharField(max_length=10)