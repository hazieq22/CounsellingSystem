from django.db import models

# Create your models here.
class Student(models.Model):
    studentID = models.CharField(max_length=15,primary_key=True)
    studentName = models.TextField(max_length=50)
    studentPhone = models.TextField(max_length=50)
    studentEmail = models.TextField(max_length=50)
    studentPassword = models.TextField(max_length=20)

class Counsellor(models.Model):
    counsellorID = models.CharField(max_length=15,primary_key=True)
    counsellorName = models.TextField(max_length=50)
    counsellorPhone = models.TextField(max_length=50)
    counsellorEmail = models.TextField(max_length=50)
    counsellorPassword = models.TextField(max_length=20)

class Session(models.Model):
    sessionID = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    reason = models.TextField(max_length=50)
    status = models.TextField(max_length=20, default="Pending")
    
class Detail(models.Model):
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE)
    sessionID = models.ForeignKey(Session,on_delete=models.CASCADE)
    details = models.TextField(max_length=100 ,null = True,default='none')
    followup = models.TextField(max_length=10,default='none')