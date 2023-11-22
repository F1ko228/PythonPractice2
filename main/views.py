from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.urls import reverse
from django import forms

from main.models import Application, ApplicationCategory, ApplicationStatus
from main.forms import ApplicationCreateForm
# Create your views here.

def index(request):
    context = {
        'title': 'Design.Pro'
    }
    return render(request, "main/index.html", context)

def applications(request, category_id=None, page=1, status_id=3):
    context = {
        'title': 'Design.PRO - Заявки',
        'categories': ApplicationCategory.objects.all(),
        'statuses': ApplicationStatus.objects.all(),
    }
    if category_id:
        applications = Application.objects.filter(category_id=category_id, status_id=status_id)
    else:
        applications = Application.objects.filter(status_id=status_id)
    paginator = Paginator(applications, 4)
    applications_paginator = paginator.page(page)
    context.update({'applications': applications_paginator})
    return render(request, 'main/applications.html', context)

@login_required
def application_delete(request, id):
    usersapplications = Application.objects.get(id=id)
    usersapplications.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def application_create(request):
    user = request.user
    if request.method == 'POST':
        form = ApplicationCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=True)
            form_instance.author = user
            form_instance.save()

            messages.success(request, 'Заявка успешно создана!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = ApplicationCreateForm(instance=user)
    context = {'form': form, 'title': 'Создание заявки'}
    print(user)
    return render(request, 'main/applicationcreate.html', context)