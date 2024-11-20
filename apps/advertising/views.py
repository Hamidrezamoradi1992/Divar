from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from apps.advertising.models import Advertising,SaveValueField,Category,FieldCategory,City,State
# Create your views here.
class AllAdvertisingView(ListAPIView):
    """
        - view all advertising

        {



        }

    """
    queryset = Advertising.objects.all().order_by('-created_at')
    serializer_class = []
    permission_classes = []

