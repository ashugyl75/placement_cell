from django.db import models
from users.models import Users

# django smtp email password jjji zcxg qanv ivpt

# Create your models here.


class RecruiterInfo(models.Model):  # 'id' is primary key
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    jobRole = models.CharField(max_length=50, null=True, blank=True)
    dateOfJoining = models.DateField(null=True, blank=True)
    packageOffered = models.CharField(max_length=50, null=True,
                                      blank=False)  # lets see later if we want it in integer or float instead
    totalRounds = models.IntegerField()


class StudentConsent(models.Model):  # 'id' is primary key
    recruiter = models.ForeignKey(RecruiterInfo, on_delete=models.CASCADE)  # FK Recruiter
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # FK users
    consent = models.BooleanField(default=False)
    isHired = models.BooleanField(default=False)


class SelectedStudents(models.Model):  # 'id' is the primary key
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # FK users
    recruiter = models.ForeignKey(RecruiterInfo, on_delete=models.CASCADE)  # FK Recruiter
    roundQualifiedFor = models.IntegerField()


