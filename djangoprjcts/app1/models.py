from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    def __str__(self):
        return self.name

class register(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    mark=models.IntegerField()
    username=models.CharField(max_length=30)
    password=models.IntegerField()
    image=models.FileField()
    def __str__(self):
        return self.name

class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.IntegerField()
    def __str__(self):
        return self.username