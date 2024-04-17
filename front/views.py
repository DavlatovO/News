from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    regions = models.Region.objects.all()
    categories = models.Category.objects.all()
    context = {
        'regions':regions,
        'categories':categories
    }

    return render(request, 'front/index.html', context)



def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard:index')
        else:
            # Add the following line to render the login template with an error message
            return render(request, 'dashboard/auth/login.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'dashboard/auth/login.html')
