from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile

def profile(request, username):
    user = User.objects.get(username=username)
    user_profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'people/profile.html', {'user': user, 'user_profile': user_profile})

def edit_profile(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'people/edit_profile.html', {'form': form, 'username': username})
