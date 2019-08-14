from django.db import models
from multiselectfield import MultiSelectField

class EnquiryData(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)

    COURSES_CHOICES=(
        ('py','Python'),
        ('dj','Djang'),
        ('ui','UI'),
        ('ra','Rest Api')
    )
    courses = MultiSelectField(max_length=200,choices=COURSES_CHOICES)
    BRANCHES_CHOICES=(
        ('hyd','Hyderabad'),
        ('bang','Bangalore'),
        ('che','Chennai'),
        ('pune','Pune'),
    )
    branches = MultiSelectField(max_length=200,choices=BRANCHES_CHOICES)

    gender = models.CharField(max_length=50)
    startdate = models.DateField(max_length=50)

