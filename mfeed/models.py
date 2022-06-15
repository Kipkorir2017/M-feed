from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.install python3-djangoinstall python3-django

# class models
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)   
    def __str__(self):
        return self.name
  
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()


class Survey(models.Model):
    name=models.CharField(max_length=200)
    profile=models.ForeignKey(User,on_delete=models.CASCADE)
    organisation=models.CharField(max_length=200)
    resp=models.IntegerField()
    quantity = models.IntegerField(max_length=10000)
    date=models.DateField(blank=False)
    action=models.BooleanField(blank=False)


    def __str__(self):
        return self.name
  
    def save_survey(self):
        self.save()
    
    def delete_survey(self):
        self.delete()



class Reports(models.Model):
    type = models.CharField(max_length=200)
    survey=models.ForeignKey(Survey,on_delete=models.CASCADE,null=True)
    survey_name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
  
    def save_report(self):
        self.save()
    
    def delete_report(self):
        self.delete()