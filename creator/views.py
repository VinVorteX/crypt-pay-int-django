from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Creator
from .forms import CreatorForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('creator:login')
    else:
        form = UserCreationForm()
    return render(request, 'creator/signup.html', {
        'form': form
    })

def creators(request):
    creators = Creator.objects.all()
    return render(request, 'creator/creators.html', {
        'creators': creators
    })

def edit(request):
    # if request.method == 'POST':
    #     form = CreatorForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Page edited successfully')
    # else:
    #     form = CreatorForm()
    try:
        creator = request.user.creator
        if request.method == 'POST':
            form = CreatorForm(request.POST, request.FILES, instance=creator)

            if form.is_valid():
                form.save()

                return redirect('core:index')
        else:
            form = CreatorForm(instance = creator)
    except Exception as e:
        if request.method == 'POST':
            form = CreatorForm(request.POST, request.FILES)

            if form.is_valid():
                creator = form.save(commit = False)
                creator.user = request.user
                creator.save()

                return redirect('core:index')
        else:
            form = CreatorForm()

    return render(request, 'creator/edit.html', {
        'form': form
    })
