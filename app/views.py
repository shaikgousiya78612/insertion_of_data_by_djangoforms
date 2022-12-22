from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_school(request):
    form=SchoolForm()
    d={'form':form}
    if request.method=="POST":
        form_data=SchoolForm(request.POST)
        if form_data.is_valid():
            N=form_data.cleaned_data['Name']
            P=form_data.cleaned_data['Principal']
            L=form_data.cleaned_data['Location']
            S=School.objects.get_or_create(Name=N,Principal=P,Location=L)[0]
            S.save()
            return HttpResponse('data is inserted successfully') 


    return render(request,'insert_school.html',d)