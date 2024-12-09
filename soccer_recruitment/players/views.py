from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm, SignInForm


def home(request):
    return render(request, 'home.html')


def soccer_scholarships(request):
    return render(request, 'soccer_scholarships.html')


def about_us(request):
    return render(request, 'about_us.html')


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


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            # Extract cleaned data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('home')  # Redirect to the home page after login
            else:
                messages.error(request, "Invalid email or password.")
                return render(request, 'signin.html', {'form': form})
        else:
            # Handle form validation errors
            return render(request, 'signin.html', {'form': form})

    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})
