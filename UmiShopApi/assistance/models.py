from django.db import models

# Create your models here.


class Assistance(models.Model):
    email = models.CharField(max_length=100, blank=False)
    topic = models.CharField(max_length=100, blank=False)
