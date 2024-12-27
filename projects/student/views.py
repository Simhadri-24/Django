from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import student

def index(request):
    return HttpResponse("Welcome to student form")
def stud_post(request):
    if request.method=='POST':
        try:
            rno=request.POST['rno']
            name=request.POST['name']
            m1=int(request.POST['m1'])
            m2=int(request.POST['m2'])
            m3=int(request.POST['m3'])
            if m1 < 0 or m2 < 0 or m3 < 0:
                raise ValueError("Marks cannot be negative.")
            if m1 > 100 or m2 > 100 or m3 > 100:
                raise ValueError("Marks cannot be greater than 100.")
            s = student(rno=rno, name=name, m1=m1, m2=m2, m3=m3)
            s.save()

            # Display student details
            return render(request, 'stud_post.html', {'s': s})
        except ValueError as e:
            return HttpResponse(f"Error: {e.message}")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")
    return render(request,'stud_form.html')
def stud_archieve(request):
    stu=student.objects.all().order_by('-total')
    return render(request,'stud_archieve.html',{'stu':stu})
        