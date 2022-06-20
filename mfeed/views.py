from django.shortcuts import render
from django.http.response import JsonResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework import status
# from .serializers import MotivationSerializer, MotivationPostSerializer, ReviewSerializer,CategorySerializer, ProfileSerializer
from .models import Profile,Survey,Comments,Reports
from django.contrib.auth.decorators import user_passes_test
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from django.http import Http404
# from .email import send_welcome_email
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from .renderers import UserJSONRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
# from .serializers import (
#     UserRegistrationSerializer,
#     UserLoginSerializer,
#     UserListSerializer,
#     ProfileSerializer,
#     SubscriptionSerializer,
#     SuperUserSerializer,
#     ActiveUserSerializer,
#     ReviewThreadSerializer,
#     WishListSerializer,
#     UserUpdateSerializer
# )

from .serialzers import (
    UserRegistrationSerializer,
    LoginSerializer
    )

# Create your views here.


class AuthUserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    renderer_class = UserJSONRenderer
    permission_classes = (AllowAny, )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data,
            }
            return Response(response, status=status_code)

# class AuthUserLoginView(APIView):
#     serializer_class = LoginSerializer
#     renderer_class = UserJSONRenderer
#     permission_classes = (AllowAny, )
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)
#         if valid:
#             status_code = status.HTTP_200_OK
#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'User logged in successfully',
#                 'authenticatedUser': {
#                     'email': serializer.data['email'],
#                 }
#             }
#             return Response(response, status=status_code)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_class = UserJSONRenderer
    serializer_class = LoginSerializer

    def post(self, request):
        # user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# jwt
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
