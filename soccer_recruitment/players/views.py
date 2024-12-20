# INF601 - Advanced Programming in Python
# Marcos German
# Final Project

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm, SignInForm, PlayerForm, UploadDocumentsForm
from .models import Player


# Register View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Create User
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            # Create Player instance for the user
            player = Player.objects.create(
                user=user,
            )
            player.save()

            messages.success(request, "You have been successfully registered.")
            return redirect('signin')  # Redirect to login page after successful registration

        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# Sign In View
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)  # This logs the user in
                messages.success(request, "You have successfully logged in.")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid email or password.")
                return render(request, 'signin.html', {'form': form})
        else:
            return render(request, 'signin.html', {'form': form})

    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})


# Home Page View
def home(request):
    return render(request, 'home.html')


# Soccer Scholarships Page View
def soccer_scholarships(request):
    return render(request, 'soccer_scholarships.html')


# About Us Page View
def about_us(request):
    return render(request, 'about_us.html')


# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


# Requisites View
@login_required
def requisites(request):
    try:
        player = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        # Handle the case where the Player does not exist
        messages.warning(request, "You don't have a player profile yet. Please complete your registration.")
        return redirect('register')  # Redirect to the registration page if the player doesn't exist

    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, "Your requisites have been saved successfully.")
            return redirect('tasks')  # Redirect to the tasks page after requisites are filled
        else:
            messages.error(request, "Please complete all the required fields.")
            return render(request, 'requisites.html', {'form': form})

    else:
        form = PlayerForm(instance=player)  # Prefill the form with existing player data
    return render(request, 'requisites.html', {'form': form})

# Tasks Page View
@login_required
def tasks(request):
    try:
        player = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.warning(request, "You don't have a player profile yet. Please complete your registration.")
        return redirect('requisites')

    if request.method == 'POST':
        form = UploadDocumentsForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, "Your documents have been uploaded successfully.")
            return redirect('dashboard')  # Redirect to the dashboard or tasks page after successful upload
        else:
            messages.error(request, "Please check the uploaded files.")
            return render(request, 'tasks.html', {'form': form})

    else:
        form = UploadDocumentsForm(instance=player)  # Prefill the form with existing player data
    return render(request, 'tasks.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')
