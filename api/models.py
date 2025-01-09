from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100, default='name')  # Added default value
    age = models.IntegerField(default=0)  # Added default value
    city = models.CharField(max_length=100 , default='city')  # Added default value


class Student(models.Model):
    name = models.CharField(max_length=100, default='name')  # Added default value
    age = models.IntegerField(default=0)  # Added default value
    city = models.CharField(max_length=100 , default='city')  # Added default value
