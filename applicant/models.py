from django.db import models

class Employee(models.Model):
    id = models.AutoField(name="id", primary_key=True)
    ename = models.TextField(name="ename", max_length=100)
    email = models.TextField(name="email", max_length=100)
    gender = models.TextField(name="gender", max_length=6)
    qualification = models.TextField(name="qualification", max_length=100)
    dob = models.TextField(name="dob", max_length=20)
    phone = models.TextField(name="phone", max_length=20)
    status = models.BooleanField(name="status", default=True)
    
    def __init__(self,name,mail,gender,qual,dob,phone):
        self.ename = name
        self.gender = gender
        self.phone = phone
        self.email = mail
        self.qualification = qual
        self.dob = dob
    
    def __str__(self):
        return f'Employee: [{self.ename}, {self.email}, {self.phone}, {self.qualification}]\n'