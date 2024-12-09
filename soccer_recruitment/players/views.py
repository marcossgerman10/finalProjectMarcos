from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm, SignInForm, PlayerForm
from .models import Player  # Ensure Player model is created


# Home Page View
def home(request):
    return render(request, 'home.html')


# Soccer Scholarships Page View
def soccer_scholarships(request):
    return render(request, 'soccer_scholarships.html')


# About Us Page View
def about_us(request):
    return render(request, 'about_us.html')


# Register Page View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Extract cleaned data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if email already exists (handled in form, so just save user)
            user = User.objects.create_user(
                username=email,  # Required field in Django User model
                email=email,
                password=password,
                first_name=form.cleaned_data['name'],
                last_name=form.cleaned_data['surname']
            )
            user.save()

            messages.success(request, "You have been successfully registered.")
            return redirect('signin')  # Redirect to login page after successful registration

        else:
            # Handle form validation errors
            return render(request, 'register.html', {'form': form})

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# Sign In Page View
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('dashboard')  # Redirect to the dashboard page
            else:
                messages.error(request, "Invalid email or password.")
                return render(request, 'signin.html', {'form': form})
        else:
            return render(request, 'signin.html', {'form': form})

    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})


# Dashboard View (Protected by login_required)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to the home page after logout


# Requisites View (Protected by login_required)
@login_required
def requisites(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user  # Associate player with logged-in user
            player.save()
            messages.success(request, "Your requisites have been saved successfully.")
            return redirect('tasks')  # Redirect to the tasks page after requisites are filled
        else:
            messages.error(request, "Please complete all the required fields.")
            return render(request, 'requisites.html', {'form': form})

    else:
        form = PlayerForm()  # Empty form for GET request
    return render(request, 'requisites.html', {'form': form})


# Tasks Page View (Protected by login_required)
@login_required
def tasks(request):
    return render(request, 'tasks.html')
