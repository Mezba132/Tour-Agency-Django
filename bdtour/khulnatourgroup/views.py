from django.shortcuts import render
from .models import TourPackage, UserInfo

# Create your views here.


def index(request):
    return render(request, 'django_app/index.html')


def welcome(request):
    tourPackage = TourPackage.objects.all()  # pylint: disable=no-member
    context = {
        'tourPackages': tourPackage
    }
    return render(request, 'tours/index.html', context)
