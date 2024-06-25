from django.shortcuts import render, redirect
from .forms import StudentForm 

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = StudentForm()
    
    return render(request, 'model_app/home.html', {'form': form})
