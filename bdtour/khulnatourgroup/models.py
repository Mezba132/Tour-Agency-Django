from django.db import models

# Create your models here.


class TourPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.name} - {self.duration_days} days - ${self.price}")


class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return (f"{self.name} - {self.email} - {self.age} years")
