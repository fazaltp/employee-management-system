from django.db import models



class Employee(models.Model):

    DEPARTMENTS = [
        ('HR', 'HR'),
        ('Finance', 'Finance'),
        ('Sales', 'Sales'),
        ('IT', 'IT'),
        ('Marketing', 'Marketing'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100,choices=DEPARTMENTS)
    salary = models.FloatField()
    joining_date = models.DateField()

    def __str__(self):
        return self.name