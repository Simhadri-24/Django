from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate #User Login

from studapp.models import Student, StudentForm # Models
from studapp.models import LoginForm #User Login


from django.template import loader
from django.urls import reverse


# Create your views here.
'''
#simple view
def home(request):
    hl="<h1>Student Application</h1>\n Home page"
    return HttpResponse(hl)
'''
#view : base template
def home(request):
    return render(request,'index.html',{})

#Read all students
def studentlist(request):
    st=Student.objects.all()
    return render(request,'listall.html',{'students':st})
#CRUD operations  
#Create a student
def createst(request):
    if request.method == 'POST':
        frm = StudentForm(request.POST)
        if frm.is_valid():
            nwst=frm.save() #form input save
            nwst.save()# db table save
        return render(request,'studentfrm.html',{'newstudent':nwst,'frm':StudentForm()})
    else:
        return render(request,'studentfrm.html',{'frm':StudentForm()})

#Read single/specific student
def studentdetails(request, id):
    mymember = Student.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {'mymember': mymember,}
    return HttpResponse(template.render(context, request))

#Update a student
def updatest(request, id):
    st=Student.objects.get(id=id)
    if request.method == 'POST':
        frm = StudentForm(request.POST, instance=st)
        if frm.is_valid():
            studupt=frm.save() #form input save
            studupt.save()# db table save
            return HttpResponseRedirect(reverse('studentlist'))
    else:
        frm = StudentForm(instance=st)
    return render(request,'studentupdate.html',{'frm':frm})


#Delete a student
def deletest(request, id):
    st = Student.objects.get(id=id)
    st.delete()
    return HttpResponseRedirect(reverse('studentlist'))

#Search a student by name
def search(request):
    #Search a specific entry
    if request.method == 'POST':
        sname=request.POST['name']
        st=Student.objects.filter(name__contains=sname)
        return render(request,'studentsrch.html',{'results':sname,'students':st})
    else:
        return render(request,'studentsrch.html',{})

'''
#login
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('studentlist')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})
'''
