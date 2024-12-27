from django.shortcuts import render,redirect

# Create your views here.
from .models import Personal,Mark
from .form import PersonalForm,MarkForm

def insert(request):
    if request.method=="POST":
        pform=PersonalForm(request.POST)
        mform=MarkForm(request.POST)
        if pform.is_valid() and mform.is_valid():
            pformi=pform.save()
            mformi=mform.save()
            mformi.appid=pformi.appid
            mform.save()
            return redirect('display')
    else:
        pform=PersonalForm()
        mform=MarkForm()
        return render(request,"student.html",{'pform':pform,'mform':mform})
def display(request):
    students=Mark.objects.order_by('-total')
    return render(request,"display.html",{'students':students})