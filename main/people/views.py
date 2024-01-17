from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile

def profile(request, username):
    user = User.objects.get(username=username)
    try:
        user_profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        user_profile = None  # Обработайте случай, когда профиль не существует
    return render(request, 'people/profile.html', {'user': user, 'user_profile': user_profile})


@login_required
def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('people:profile', username=request.user.username)
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'people/edit_profile.html', {'form': form})
