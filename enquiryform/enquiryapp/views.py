from django.shortcuts import render
from django.http.response import HttpResponse
from .models import EnquiryData
from .forms import EnquiryForm

def enquiryview(request):
    if request.method=='POST':
        eform = EnquiryForm(request.POST)
        if eform.is_valid():
            name = eform.cleaned_data.get('name')
            email = eform.cleaned_data.get('email')
            mobile = eform.cleaned_data.get('mobile')
            courses = eform.cleaned_data.get('courses')
            branches = eform.cleaned_data.get('branches')
            gender = eform.cleaned_data.get('gender')
            startdate = eform.cleaned_data.get('startdate')

            data = EnquiryData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                branches=branches,
                gender=gender,
                startdate=startdate
            )
            data.save()
            eform = EnquiryForm()
            return render(request,'enquiry.html',{'eform':eform})
        else:
            return HttpResponse('Invalid user data')
    else:
        eform = EnquiryForm()
        return render(request,'enquiry.html',{'eform':eform})