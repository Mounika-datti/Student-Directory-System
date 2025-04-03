from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True,default='None')
    department = models.CharField(max_length=100, default='None')
    year_of_study = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_no})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    # Add other profile fields here

    def __str__(self):
        return self.user.username