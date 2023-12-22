# django_project/users/views.py
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.

# email generation imports
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from users.models import Users
from main.models import RecruiterInfo, StudentConsent



def home(request):
    uid = request.user.id # fetching the current logged in user's id
    
    # if the user checks consent form and then click on update database button
    if request.method == 'POST':
        consent = request.POST.getlist('consent')
        student_consents_to_update = StudentConsent.objects.filter(user=uid, recruiter__in=consent)
        for student_consent in student_consents_to_update:
            student_consent.consent = True
        StudentConsent.objects.bulk_update(student_consents_to_update, ['consent'])    # Bulk update all StudentConsent objects


    # parse all the new recruiters that the user has not applied to yet and whose date of apply has not passed
    recruiters_with_none_consent = StudentConsent.objects.filter(user=uid,consent=False).values("recruiter")
    newRecruiters = RecruiterInfo.objects.filter(id__in=recruiters_with_none_consent, lastDateToApply__gte=timezone.now())
    return render(request=request, template_name="main/home.html", context={'newRecruiters': newRecruiters})