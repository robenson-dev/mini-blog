from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.decorators import super_blogger_required

@login_required
def details(request):
    return HttpResponse('hello world ')
