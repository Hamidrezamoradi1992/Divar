from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView, View
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from validate_email import validate_email
from django.core.cache import cache
from apps.account.utils.utils import Utils
from apps.account.models import User
from service.email import EmailService


# Create your views here.
class SignUpView(APIView):
    permission_classes = []

    def post(self, request):

        email = request.data['email']
        if not validate_email(email):
            return Response({'message': 'email not valid'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not (code := cache.get(email)):
            code = Utils.code_generator()

        EmailService(subject='verify code',
                     template_name='mail/welcome.html',
                     to_email=[email],
                     context={'code': code}).send()
        cache.set(email, code, 120)

        return Response({'redirect': f'http://localhost:8000/accounts/verify/{email}'},
                        status=status.HTTP_201_CREATED)


class VerifyEmailView(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data['email']
        codes = request.data['code']
        if not (code := cache.get(email)):
            return Response({'message': 'email not valid'},
                            status=status.HTTP_400_BAD_REQUEST)
        if code == codes:
            user, _ = User.objects.get_or_create(email=email)
            refresh = RefreshToken.for_user(user=user)

            response = Response({'message': 'email already verified'},
                                status=status.HTTP_200_OK)
            response.set_cookie(key='access', value=refresh.access_token, expires=7200)
            response.set_cookie(key='refresh', value=refresh, expires=864000)

            return response


class LoginView(APIView):
    def get(self, request):
        print(request.user.is_authenticated)
        return Response({'message': 'logged in'})
