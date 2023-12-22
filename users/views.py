# django_project/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.

# email generation imports
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token


# this function needs to be called when a new user is to be created
def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('activate_account_email.html',
                               {'user': user.username, 'domain': get_current_site(request).domain,
                                   'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                   'token': account_activation_token.make_token(user),
                                   'protocol': 'https' if request.is_secure() else 'http'})
    email = EmailMessage(mail_subject, message, to = [to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


# this function will be called when the user clicks on the link sent to email
def activate(request, uidb64, token):
    return redirect('homepage')


def signIn(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/home")
            
        else:
            
        
            return HttpResponse("fail")


def signOut(request):
    if request.user.is_authenticated:    
        logout(request)
        return HttpResponse("<strong>logout successful.<a href='/'> Go to Login page</a></strong>")
    else:
        return HttpResponse("<strong>invalid request</strong>")
    

def signUp(request):
    User = get_user_model()
    # Logged-in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        dob = request.POST.get('dob', '')
        tenthMarks = request.POST.get('tenthMarks', '')
        twelvethMarks = request.POST.get('twelvethMarks', '')
        graduation = request.POST.get('graduation', '')
        motherName = request.POST.get('motherName', '')
        fatherName = request.POST.get('fatherName', '')
        resume = request.FILES.get('resume', None)  # For file upload
        gender = request.POST.get('gender', '')
        user = User.objects.create_user(first_name = firstName, last_name = lastName, username = username,
                                        email = email, password = password1, dob = dob, tenthMarks = tenthMarks,
                                        twelvethMarks = twelvethMarks, graduation = graduation, motherName = motherName,
                                        fatherName = fatherName, resume = resume, gender = gender)

    # return render(request = request, template_name = "users/signup.html", context = {})
        return HttpResponse("done")
    return HttpResponse("no get request allowed")


def signInUp(request):
    form_fields = [
    {
        'name': 'firstName',
        'icon': 'fas fa-user',
        'type': 'text',
        'placeholder': 'First Name',
        'min': '',
        'max': '',
    },
    {
        'name': 'lastName',
        'icon': 'fas fa-user',
        'type': 'text',
        'placeholder': 'Last Name',
        'min': '',
        'max': '',
    },
    {
        'name': 'gender',
        'icon': 'fas fa-venus-mars'
    },
    {
        'name': 'username',
        'icon': 'fas fa-user',
        'type': 'text',
        'placeholder': 'Username',
        'min': '8',
        'max': '12',
    },
    {
        'name': 'email',
        'icon': 'fas fa-envelope',
        'type': 'email',
        'placeholder': 'Email address',
        'min': '3',
        'max': '50',
    },
    {
        'name': 'password1',
        'icon': 'fas fa-lock',
        'type': 'password',
        'placeholder': 'Password',
        'min': '8',
        'max': '32',
    },
    {
        'name': 'password2',
        'icon': 'fas fa-lock',
        'type': 'password',
        'placeholder': 'Confirm Password',
        'min': '8',
        'max': '32',
    },
    {
        'name': 'dob',
        'icon': 'fas fa-calendar',
        'type': 'date',
        'placeholder': 'Date of Birth',
        'min': '1900-01-01',
        'max': '2005-12-31',
    },
    {
        'name': 'tenthMarks',
        'icon': 'fas fa-percentage',
        'type': 'number',
        'placeholder': '10th Marks',
        'min': '0',
        'max': '100',
    },
    {
        'name': 'twelvethMarks',
        'icon': 'fas fa-percentage',
        'type': 'number',
        'placeholder': '12th Marks',
        'min': '0',
        'max': '100',
    },
    {
        'name': 'graduation',
        'icon': 'fas fa-percentage',
        'type': 'number',
        'placeholder': 'Graduation Marks',
        'min': '0',
        'max': '100',
    },
    {
        'name': 'motherName',
        'icon': 'fas fa-female',
        'type': 'text',
        'placeholder': "Mother's Name",
        'min': '0',
        'max': '50',
    },
    {
        'name': 'fatherName',
        'icon': 'fas fa-male',
        'type': 'text',
        'placeholder': "Father's Name",
        'min': '0',
        'max': '50',
    },
    {
        'name': 'resume',
        'icon': 'fas fa-file',
        'type': 'file',
        'placeholder': 'Resume(PDF ONLY)',
        'accept': '.pdf'

    }
]

    return render(request=request, template_name='signInUp.html',context={'form_fields':form_fields})