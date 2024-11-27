from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MainFavoriteSerializer


# Create your views here.

class AddFavoriteView(APIView):
    serializers_class = MainFavoriteSerializer

    def post(self, request):
        serializer = self.serializers_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
