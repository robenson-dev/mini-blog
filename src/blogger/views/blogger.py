from django.shortcuts import render, redirect


def home(request):

    if request.user.is_authenticated:
        if request.user.is_super_blogger:
            return redirect('legendary:legendary-dashboard')
        else:
            return redirect('member:member-detail')
    else:
        return redirect('users:signin')
