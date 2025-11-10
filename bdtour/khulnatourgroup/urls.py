from django.urls import path
from .views import index, welcome, contact, contact_success

urlpatterns = [
    path('welcome', welcome, name='welcome'),
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('contact/success', contact_success, name='contact_success'),
]
