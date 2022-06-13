from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework  import  viewsets,status,generics,permissions,filters,serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
import jwt, datetime
from django.shortcuts import  render
import requests
import json
# from decouple import config
from django.core import serializers
from .models import User,Survey,Reports,Profile
from .serializers import  ProfileSerializer,SurveySerializer,ReportsSerializer,UsersSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileList(APIView):
    def get(self, request, format=None):
        profile_all = Profile.objects.all()
        serializers = ProfileSerializer(profile_all, many=True)
        return Response(serializers.data)


# class ProfileList(viewsets.ModelViewSet):
#         queryset=Profile.objects.all()
#         serializer_class=ProfileSerializer
#         permission_classes = (IsAuthenticatedOrReadOnly,)

class SurveyList(viewsets.ModelViewSet):
        queryset=Survey.objects.all()
        serializer_class=SurveySerializer
    
    
class ReportsList(viewsets.ModelViewSet):
        queryset=Reports.objects.all()
        serializer_class=ReportsSerializer
    

class RegisterView(APIView):
        def post(self, request):
            serializer = UsersSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class LoginView(APIView):
        def post(self, request):
            email = request.data['email']
            password = request.data['password']

            user = User.objects.filter(email=email).first()

            if user is None:
                raise AuthenticationFailed('User not found!')

            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password!')

            payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

            response = Response()

            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
            'email':email,
            'jwt': token
            }
            return response


class UserView(APIView):

        def get(self, request):
            token = request.COOKIES.get('jwt')

            if not token:
                raise AuthenticationFailed('Unauthenticated!')

            try:
                payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated!')

            user = User.objects.filter(id=payload['id']).first()
            serializer = UsersSerializer(user)
            return Response(serializer.data)

class LogoutView(APIView):
        def post(self, request):
            response = Response()
            response.delete_cookie('jwt')
            response.data = {
            'message': 'success'
            }
            return response