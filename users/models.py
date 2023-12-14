from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Users(AbstractUser):
    gender = models.CharField(max_length=20, null=True, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    dob = models.DateField(null=True)
    tenthMarks = models.FloatField(null=True)  # solve for CGPA or percentage
    twelvethMarks = models.FloatField(null=True)
    graduation = models.FloatField(null= True)
    motherName = models.CharField(max_length=100, null=True)
    fatherName = models.CharField(max_length=100, null=True)
    resume = models.FileField(upload_to='resume/')  # need to define a MEDIA_ROOT path in settings.py # only accept pdf format

    def __str__(self):
        return self.username


