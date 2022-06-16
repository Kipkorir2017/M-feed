from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Survey,Profile,Reports
# Register your models here.
admin.site.register(Survey)
admin.site.register(Profile)
admin.site.register(Reports)