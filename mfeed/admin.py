from django.contrib import admin
from .models import FeedUser,Comments,Survey,Reports,Organization,Profile

# Register your models here.

admin.site.register(FeedUser)
admin.site.register(Comments)
admin.site.register(Survey)
admin.site.register(Reports)
admin.site.register(Organization)
admin.site.register(Profile)