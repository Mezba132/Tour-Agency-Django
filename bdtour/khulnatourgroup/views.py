from django.shortcuts import render
from .models import TourPackage, UserInfo
from .forms import ContactForm

# Create your views here.


def index(request):
    return render(request, 'django_app/index.html')


def welcome(request):
    tourPackage = TourPackage.objects.all()  # pylint: disable=no-member
    context = {
        'tourPackages': tourPackage
    }
    return render(request, 'tours/index.html', context)


def home_view(request):
    return render(request, 'django_app/home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return render(request, 'django_app/contact_success.html')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'django_app/contact.html', context)


def contact_success(request):
    return render(request, 'django_app/contact_success.html')
