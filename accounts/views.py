from django.shortcuts import render
from .models import Profile
# Create your views here.


def signup(request):
    pass










def profile(request):
    profile = profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html',{'profile': profile})


def profile_edit(request):
    
    return render(request, 'accounts/profile_edit.html',{})
















