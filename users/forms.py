from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# check out django crispy forms


class UserRegistrationForm(UserCreationForm):

    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), label='Gender', required=True)
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    dob = forms.DateField(label='Date of Birth', required=True, help_text='YYYY-MM-DD')
    tenth_marks = forms.FloatField(label='10th Marks', required=True)  # CGPA or percentage
    twelfth_marks = forms.FloatField(label='12th Marks', required=True)
    graduation_marks = forms.FloatField(label='Graduation Marks', required=True)
    mother_name = forms.CharField(label='Mother\'s Name', max_length=100, required=True)
    father_name = forms.CharField(label='Father\'s Name', max_length=100, required=True)
    resume = forms.FileField(label='Resume', required=False)  # Defined MEDIA_ROOT path in settings.py

    class Meta:
        model = get_user_model()  # because we are using custom user model we need to fetch it everytime
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'dob', 'tenth_marks',
                  'twelfth_marks', 'graduation_marks', 'mother_name', 'father_name', 'resume']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.gender = self.cleaned_data['gender']
        user.email = self.cleaned_data['email']
        user.dob = self.cleaned_data['dob']
        user.tenth_marks = self.cleaned_data['tenth_marks']
        user.twelfth_marks = self.cleaned_data['twelfth_marks']
        user.graduation_marks = self.cleaned_data['graduation_marks']
        user.mother_name = self.cleaned_data['mother_name']
        user.father_name = self.cleaned_data['father_name']
        user.resume = self.cleaned_data['resume']
        if commit:
            user.save()
        return user
