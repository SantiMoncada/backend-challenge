from django.db import models

# Create your models here.


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False, unique=True)
    phone = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=250, blank=False)

    class Meta:
        ordering = ['created']
