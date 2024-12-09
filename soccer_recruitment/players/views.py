# players/views.py
from django.shortcuts import render, redirect
from .forms import PlayerRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('signin')
    else:
        form = PlayerRegistrationForm()
    return render(request, 'register.html', {'form': form})

def signin(request):
    return render(request, 'signin.html')
