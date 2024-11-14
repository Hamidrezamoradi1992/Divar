from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView, View
from rest_framework import status
from django.core.validators import EmailValidator
from validate_email import validate_email
from django.core.cache import cache
from random import randint

from apps.account.models import User
from service.email import EmailService


# Create your views here.
class SignUpView(APIView):
    @staticmethod
    def _code_generator():
        return str(randint(100000, 999999))

    def post(self, request):
        print('post')
        email = request.data['email']
        if not validate_email(email):
            return Response({'message': 'email not valid'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not (code := cache.get(email)):
            code = self._code_generator()

        EmailService(subject='verify code',
                     template_name='mail/welcome.html',
                     to_email=[email],
                     context={'code': code}).send()
        cache.set(email, code, 120)

        return Response({'redirect': f'http://localhost:8000/accounts/verify/{email}'},
                        status=status.HTTP_201_CREATED)


class VerifyEmailView(APIView):
    def post(self, request):
        email = request.data['email']
        codes = request.data['code']
        if not (code := cache.get(email)):
            return Response({'message': 'email not valid'},
                            status=status.HTTP_400_BAD_REQUEST)
        if code == codes:
            User.objects.get_or_create(email=email)
            res= Response({'message': 'email already verified'},
                          status=status.HTTP_200_OK)
            res.set_cookie("name", "sina", 100)
            return res


