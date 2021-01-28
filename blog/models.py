from django.db import models
from datetime import datetime
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12)
    adr = models.CharField(max_length=200, default='Ratanpur')
    desc = models.TextField()
    # date = models.DateField(default=datetime.today())

    def __str__(self):
        return self.name
