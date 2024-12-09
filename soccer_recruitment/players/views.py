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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            # Check if passwords match
            if password != password2:
                messages.error(request, "Passwords do not match.")
                return render(request, 'register.html', {'form': form})

            # Check if email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
                return render(request, 'register.html', {'form': form})

            # Create a new user
            user = User.objects.create_user(email=email, password=password)
            user.first_name = form.cleaned_data['name']
            user.last_name = form.cleaned_data['surname']
            user.save()

            messages.success(request, "You have been successfully registered.")
            return redirect('signin')  # Redirect to login page after successful registration

        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'register.html', {'form': form})

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


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
                return redirect('dashboard')  # Redirect to the dashboard or home page
            else:
                messages.error(request, "Invalid email or password.")
                return render(request, 'signin.html', {'form': form})
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'signin.html', {'form': form})

    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})
