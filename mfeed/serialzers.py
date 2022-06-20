from asyncore import read
from .models import  FeedUser,Profile
from rest_framework import fields, serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
# from .email import send_welcome_email


class UserRegistrationSerializer(serializers.ModelSerializer):

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = FeedUser
        fields = (
            'username',
            'email',
            'role',
            'password',
            'token'
        )

    def create(self, validated_data):
        auth_user = FeedUser.objects.create_user(**validated_data)
        return auth_user


class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedUser
        fields = (
            'is_superuser',
        )

class ActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedUser
        fields = (
            'is_active',
        )

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedUser
        fields = (
            'first_name',
            'last_name'
        )
    


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255,read_only=True)
    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        username = data.get('username', None)
        password = data.get('password', None)

        # Raise an exception if an
        # email is not provided.
        if username is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `email`.
        user = authenticate(username=username, password=password)

        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag is to tell us whether the user has been banned
        # or deactivated. This will almost never be the case, but
        # it is worth checking. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'role',
            'is_active',
            'is_staff',
            'is_superuser',
        )        