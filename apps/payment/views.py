from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.payment.serializers import AddLadderToOrderSerializer


# Create your views here.
class AddToOrderForLadderView(APIView):
    serializer_class = AddLadderToOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'ok'},status=status.HTTP_200_OK)
        return Response({'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
