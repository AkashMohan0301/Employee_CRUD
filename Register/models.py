from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)