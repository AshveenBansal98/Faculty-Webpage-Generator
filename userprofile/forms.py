from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import About_us
from .models import Teaching
from .models import *


class teaching_add(forms.ModelForm):
    Course = forms.CharField(max_length=200, required=True)
    Year = forms.CharField(max_length=200, required=True)
    Description = forms.CharField(max_length=300)
    class Meta:
        model = Teaching
        fields = ('Course', 'Year','Description')

class about_us_form(forms.ModelForm):
    Name = forms.CharField(max_length=60,required=True)
    Department = forms.CharField(max_length=60,required=True)
    Institute = forms.CharField(max_length=60,required=True)
    Departmental_post = forms.CharField(max_length=60 , required=True)
    Room_no = forms.CharField(max_length=10 , required=True)
    Phone = forms.CharField(max_length=15 , required=True , help_text="+91 must not be added in front")
    Email = forms.CharField(max_length=30 , required=True )
    Address = forms.CharField(max_length=50 , required=True)
    ResearchInterest = forms.CharField(max_length=80 , required=True)
    LinkedinURL = forms.CharField(max_length=80 , required=True)
    class Meta:
        model = About_us
        fields = ('Name','Department', 'Institute' , 'Departmental_post' , 'Room_no' , 'Phone' , 'Email' , 'Address'  , 'ResearchInterest' , 'LinkedinURL')

class projecting_add(forms.ModelForm):
    Topic = forms.CharField(max_length=200, required=True)
    Details = forms.CharField(max_length=200, required=True)
    Year = forms.CharField(max_length=200, required=True)
    class Meta:
        model = Projecting
        fields = ('Topic','Details', 'Year')
