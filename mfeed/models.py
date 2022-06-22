from datetime import date
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import uuid
from cloudinary.models import CloudinaryField
from .managers import CustomUserManager
from datetime import datetime as dt
from datetime import timedelta as td
# import datetime
from django.conf import settings
import jwt


# today = datetime.now()
# today.strftime('%Y-%m-%d')

class FeedUser(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    PARENT = 2

    USER_ROLE_CHOICES = (
        (ADMIN, 'Organization'),
        (PARENT, 'Parent'),
    )

    username = models.CharField(unique=True,max_length=20)
    first_name = models.CharField(max_length=30, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True,null=True)
    email = models.EmailField()
    role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES, blank=True, null=True, default=2)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    modified_by = models.EmailField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        # date_rec = datetime.strftime
        test_date = '4/25/2015'
        today = dt.now()
        delta = td(days=60)



        token = jwt.encode({
            'id': self.pk,
            # 'exp': str(delta.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

# Make two sign up sheets that allow someone to have superuser privileges

class Profile(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(FeedUser,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image',blank=True, null=True)
    profile_email = models.EmailField()
    phone_number = models.CharField(max_length=20,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Organization(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    org_name = models.CharField(max_length=200)

    def __str__(self):
        return self.org_name
class Survey(models.Model):
    school = models.CharField(max_length=20)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    statement = models.TextField(max_length=3000)
    posted_on = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

class Reports(models.Model):
    type = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)

class Comments(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    comment = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
