from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from main.models import ApplicationStatus, Application


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form, 'title': 'Design.Pro - Авторизация'}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form, 'title': 'Design.Pro - Регистрация'}
    return render(request, 'users/register.html', context)

@login_required()
def profile(request, status_id=None):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные изменены')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)

    usersapplications = Application.objects.filter(author=user)
    context = {
        'form': form,
        'title': 'Design.Pro - Личный кабинет',
        'usersapplications': usersapplications,
        'statuses': ApplicationStatus.objects.all(),
    }
    if status_id:
        usersapplications = Application.objects.filter(status_id=status_id, author=request.user)
    else:
        usersapplications = Application.objects.filter(author=user)
    context.update({'usersapplications': usersapplications})
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
