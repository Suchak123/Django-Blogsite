from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from account.forms import (
    CreateUserForm,
    # UserAuthenticationForm
)
from django.contrib.auth import views as auth_views

@login_required
def profile(request):
    context= {'profile': profile}
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

