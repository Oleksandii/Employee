from django.db import models




    


class Department(models.Model):
    name = models.CharField(max_length=30)
    countofdepartment = models.IntegerField()
    descriptionofdepartment = models.CharField(max_length=30)

class Description(models.Model):
    senioritylevel = models.CharField(max_length=30)
    countofsubordinates = models.IntegerField()




class Pseudonym(models.Model):
    pseudonym = models.CharField(max_length=30)

    
class Tasks(models.Model):
    taskName = models.CharField(max_length=30)
    taskdescription = models.CharField(max_length=30)
    


class Employees(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    age = models.IntegerField()
    pseudonym = models.OneToOneField(Pseudonym,on_delete=models.SET_NULL,null=True)
    description = models.OneToOneField(Description,on_delete=models.SET_NULL,null=True)
    tasks = models.ManyToManyField(Tasks)




# Create your models here.
