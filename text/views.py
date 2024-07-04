from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from .models import User

def user_profile(request, id=None):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('user_profile')
    else:
        form = UserForm()

    users = User.objects.all()
    return render(request, 'user_profile.html', {'form': form, 'users': users})

def user_profile_edit(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_profile')
    else:
        form = UserForm(instance=user)

    users = User.objects.all()
    return render(request, 'user_profile.html', {'form': form, 'users': users})

def delete_user(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('user_profile')
