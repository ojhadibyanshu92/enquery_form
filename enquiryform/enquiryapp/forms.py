from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Name'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Email'
            }
        )
    )
    COURSES_CHOICES = (
        ('py', 'Python'),
        ('dj','Djang'),
        ('ui', 'UI'),
        ('ra', 'Rest Api')
    )
    courses = MultiSelectFormField(max_length=200, choices=COURSES_CHOICES)
    BRANCHES_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Bangalore'),
        ('che', 'Chennai'),
        ('pune', 'Pune')
    )
    branches = MultiSelectFormField(max_length=200, choices=BRANCHES_CHOICES)

    GENDER_CHOICES=(
        ('M','Male'),
        ('f','Fenale')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=GENDER_CHOICES
    )
    y = range(2019,2022)
    startdate = forms.DateField(
        widget=forms.SelectDateWidget(years=y)
    )