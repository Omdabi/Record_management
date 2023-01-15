from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class department(models.Model):
    dept_name = models.CharField(max_length=100)


    def __str__(self):
        return self.dept_name

class teacher(models.Model):
    tname = models.CharField(max_length=100)
    tdept_name = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return self.tname


class student(models.Model):
    roll = models.PositiveIntegerField()
    sname = models.CharField(max_length=100)
    father_name= models.CharField( max_length=50)
    contact = models.IntegerField()
    sdept_name = models.ForeignKey(department, on_delete=models.CASCADE)


    def __str__(self):
        return self.sname



