from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
