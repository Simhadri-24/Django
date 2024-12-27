from django.shortcuts import render,redirect
from django.db.models import F,ExpressionWrapper,FloatField
from .models import student
from .forms import studentform

# Create your views here.
def index(request):
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_data')

    else:
        form=studentform()
        return render(request,'student.html',{'form':form})
def display_data(request):
    people=student.objects.all()
    return render(request,'display_data.html',{'people':people})
