from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import UserSignUpForm
from django.contrib.auth import (
    forms  as auth_forms,
    decorators,
    login,
    logout
)


def signup(request):

    if request.user.is_authenticated:
        return redirect('users:profile')
    else:
        if request.method == 'POST':

            form = UserSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your account has been created!')
                return redirect('users:signin')
        else:
            form = UserSignUpForm()

        return render(request, 'users/signup.html', locals())


def signin(request):

    if request.user.is_authenticated:
        return redirect('users:profile')
    else:
        if request.method == 'POST':
            form = auth_forms.AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user is not None:
                    login(request, user)
                    return redirect('users:profile')
                else:
                    messages.warning(request, f' username or password is incorrect')
        else:
            form = auth_forms.AuthenticationForm()

        return render(request, 'users/signin.html', locals())


def signout(request):
    logout(request)
    return redirect('users:signin')


@decorators.login_required(login_url='/user/signin')
def profile(request):
    return render(request, 'users/profile.html')
