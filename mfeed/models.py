from django.db import models

# Create your models here.install python3-djangoinstall python3-django
class Profile(models.Model):
    name = models.CharField()
class Survey(models.Model):
    quantity = models.IntegerField(max_length=10000)

class Reports(models.Model):
    type = models.CharField(max_length=200)

