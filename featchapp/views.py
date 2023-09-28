from django.shortcuts import render
from featchapp.models import employees
from .import forms

# Create your views here.
def emp(request):
    my_user = employees.objects.all()
    return render (request,'home.html',{'my_user': my_user})
def  students(request):
    form=forms.users()
    if request.method == 'POST':
        form=forms.users(request.POST)
        if form.is_valid():
            form.save()
    return render (request,'add.html',{'form':form})

