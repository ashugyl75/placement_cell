from django.contrib import admin
from .models import RecruiterInfo, StudentConsent, SelectedStudents
# Register your models here.
admin.site.register(RecruiterInfo)
admin.site.register(StudentConsent)
admin.site.register(SelectedStudents)
