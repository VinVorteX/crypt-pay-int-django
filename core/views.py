from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        try:
            creator = request.user.creator
        except Exception as e:
            return redirect('creator:edit')
    return render(request, 'core/index.html')


