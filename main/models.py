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
    lastDateToApply = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def isApplicationOpen(self):
        if self.lastDateToApply == None:
            return True
        return self.lastDateToApply >= timezone.now()


class StudentConsent(models.Model):  # 'id' is primary key
    recruiter = models.ForeignKey(RecruiterInfo, on_delete=models.CASCADE, related_name="studentConsent", null=True)  # FK Recruiter
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="studentConsent", null=True)  # FK users
    consent = models.BooleanField(default=False, null=True) # can be set to default false, as false can always be implied as null i.e. the student is not yet interested or the student is not interested at all
    isHired = models.BooleanField(default=None, null=True)
    
    # def __str__(self):
    #     return self.id


class SelectedStudents(models.Model):  # 'id' is the primary key
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # FK users
    recruiter = models.ForeignKey(RecruiterInfo, on_delete=models.CASCADE)  # FK Recruiter
    roundQualifiedFor = models.IntegerField()
    
    def __str__(self):
        return self.user


