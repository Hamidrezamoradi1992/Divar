from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView, View
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from validate_email import validate_email
from .models import User
from django.core.cache import cache
from apps.core.models.images import Image
from apps.account.serializers import UpdateUserSerializer, MainUserSerializer, UpdateImageUserSerializer
from apps.account.utils.utils import Utils
from service.email import EmailService
from apps.core.serializers import MainImageSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from django.contrib.contenttypes.models import ContentType


# Create your views here.


# swagger
class SignUpView(APIView):  # swagger
    """
        - sign up user input

            {

                'email': '<EMAIL>',

            }

        - sign up user output

            {

                redirect': 'http://localhost:8000/accounts/verify/{email}'

            }

    """
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


# swagger
class VerifyEmailView(APIView):  # swagger
    """
    - config verification code input


        {

            'email': '<EMAIL>',

            'code': '123456'

        }

    - config verification code output


        {

            - set cookie
                {
                    'access_token': '<KEY>',
                    'refresh_token': '<KEY>',

                }

        }
    """
    permission_classes = []

    def post(self, request):
        email = request.data['email']
        codes = request.data['code']
        if not (code := cache.get(email)):
            return Response({'message': 'email not valid'},
                            status=status.HTTP_400_BAD_REQUEST)
        if code == codes:
            user, _ = User.objects.get_or_create(email=email, password=None)
            refresh = RefreshToken.for_user(user=user)
            response = Response({'message': 'email already verified'},
                                status=status.HTTP_200_OK)
            response.set_cookie(key='access', value=refresh.access_token, expires=7200)
            response.set_cookie(key='refresh', value=refresh, expires=864000)

            return response
        return Response({'message': 'email not valid'},
                        status=status.HTTP_400_BAD_REQUEST)


# swagger
class UserProfileView(RetrieveAPIView):
    """
    - request profile view
        +  accounts/api/user/8

    - output

        {

            "id": 8,
            "email": "1243@gmail.com",
            "first_name": "",
            "last_name": "",
            "is_active": true,
            "phone": null,
            "is_kyc": false,
            "gender": null,
            "address": null,
            "age": null
        }
    """
    permission_classes = []
    serializer_class = MainUserSerializer
    queryset = User.objects.all()


# swagger
class UpdateUserView(UpdateAPIView):
    """
        - update user input
        - method put

        {

        "first_name": "",
        "last_name": "",
        "phone": "",
        "gender": null,
        "address": "",
        "age": null

        }


    output is accepted
    """

    permission_classes = []
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()

    def patch(self, request, *args, **kwargs):
        pass


# swagger
class UserImageView(APIView):
    """
        - get and update  user image

            - method get

            - REQUEST /accounts/api/update/user/image/{user_id}

            - output is accepted

            {

                    "id": 1,
                    "name": "12@gmial.com",
                    "content_type": 7,
                    "image": "/storage/media/qC8qKXt.jpg",
                    "instance_id": 7,
                    "alt": "user_image",
                    "is_cover": false

            }

        - get and update  user image

            - method patch

            - REQUEST /accounts/api/update/user/image/{user_id}

            - output is accepted

            {

                "image": "<file.jpg,png>

            }

    """

    permission_classes = []
    serializer_class = UpdateImageUserSerializer

    def get(self, request, user_id=None):
        # user_id=request.data['user_id']
        user = User.objects.filter(id=user_id)
        if user.exists():
            image = Image.objects.get(content_type=ContentType.objects.get(model='user'), instance_id=user_id)
            serializer = MainImageSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'massage': 'error'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, user_id=None):
        if not user_id:
            return Response({'message': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        user_exists = User.objects.filter(id=user_id).exists()
        if not user_exists:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            images = Image.objects.get(
                content_type=ContentType.objects.get(model='user'),
                instance_id=user_id
            )
        except Image.DoesNotExist:
            return Response({'message': 'Image not found for this user'}, status=status.HTTP_404_NOT_FOUND)
        image_file = request.data.get('image', None)
        if not image_file:
            return Response({'message': 'Image file is required'}, status=status.HTTP_400_BAD_REQUEST)

        images.image = image_file
        try:
            images.save()
        except ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Image updated successfully'}, status=status.HTTP_200_OK)
