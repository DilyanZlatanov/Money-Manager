from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from core.forms import CustomUserCreationForm, CustomLoginForm


def home(request, registration_form=None, login_form=None):
    if login_form is None:
        login_form = CustomLoginForm()
    if registration_form is None:
        registration_form = CustomUserCreationForm()
    return render(request, 'home_page.html', {
        'register_form': registration_form,
        'login_form': login_form
    })


def register_view(request):
    register_form = CustomUserCreationForm(request.POST)
    if register_form.is_valid():
        register_form.save()
        messages.success(request, "Registration successful!")
        return redirect('home')
    else:
        messages.error(request, "Registration failed.")
        return render(request, 'home_page.html', {'register_form': register_form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        login_form = CustomLoginForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials")
            return render(request, 'home_page.html', {'login_form': login_form})
    else:
        login_form = CustomLoginForm()
    return render(request, 'home_page.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})
