from django.shortcuts import render
from . import models

def index(request):
     regions = models.Region.objects.all()
     context = {
          'regions':regions
     }

     return render(request, 'front/index.html', context)
