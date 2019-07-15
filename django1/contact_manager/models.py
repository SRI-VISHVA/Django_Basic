from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(default='+91', max_length=15)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=10)
    capital = models.CharField(max_length=24)
    population = models.IntegerField()
    sea = models.BooleanField()
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name
