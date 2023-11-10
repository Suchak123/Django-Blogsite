from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from account.forms import (
    CreateUserForm,
    UserUpdateForm,
    ProfileUpdateForm
    # UserAuthenticationForm
)
from django.contrib.auth import views as auth_views

@login_required
def profile(request):
    if request.method == 'POST':
        updateForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if updateForm.is_valid() and profileForm.is_valid():
            updateForm.save()
            profileForm.save()
            messages.success(request, f'Your account have been updated!')
            return redirect('profile')
    else:
        updateForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'updateForm': updateForm,
        'profileForm': profileForm
    }
    return render(request , 'account/profile.html', context)

# def login_view(request):
#     context = {}

#     user = request.user
#     if user.is_authenticated:

#         return redirect('register')
#         form = UserAuthenticationForm
#         context['login_form'] = form
        
#     return render(request, 'account/login.html', context)

def register_view(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! Please login to continue')
            return redirect('login')
        
    else:
        form = CreateUserForm()
            # context['registration_form'] = form
    return render(request, 'account/register.html', {'form' :form})


# def logout_view(request):
#     logout(request)
#     return redirect('/')

