from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm, LoginForm, UserForm, UserProfileForm


def register(request):
    logout(request)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
            )
            messages.success(
                request, 'Account has been created! Please login below...')
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        return render(request, 'accounts/register.html', {'form': RegistrationForm()})


def login_view(request):
    logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'Welcome {user.first_name}!')
                    return redirect('accounts:profile')
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        return render(request, 'accounts/login.html', {'form': LoginForm()})
    return redirect('accounts:login')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('accounts:login')


@login_required(login_url='/login/')
def profile(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'accounts/profile.html', {'user': user})


@login_required(login_url='/login/')
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST,
                                       instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile has been Updated!')
            return redirect('accounts:profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/edit_profile.html', context)
