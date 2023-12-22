from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Users(AbstractUser):
    gender = models.CharField(max_length=20, null=True, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    dob = models.DateField(null=True, blank=True)
    tenthMarks = models.FloatField(null=True, blank=True)  # solve for CGPA or percentage
    twelvethMarks = models.FloatField(null=True, blank=True)
    graduation = models.FloatField(null= True, blank=True)
    motherName = models.CharField(max_length=100, null=True, blank=True)
    fatherName = models.CharField(max_length=100, null=True, blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)  # need to define a MEDIA_ROOT path in settings.py # only accept pdf format

    def __str__(self):
        return self.username


