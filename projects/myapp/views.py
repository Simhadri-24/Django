from django.shortcuts import render, redirect

# Create your views here.
from .forms import PersonForm
from .models import Person

def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_data')
    else:
        form = PersonForm()
    return render(request, 'index.html', {'form': form})

def display_data(request):
    people = Person.objects.all()
    return render(request, 'display_data.html', {'people': people})
