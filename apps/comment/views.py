from django.shortcuts import render
from apps.account.models import User
from apps.advertising.models import Advertising
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer

# Create your views here.

"""send massage new"""


class CommentSendView(APIView):
    '''
        - send message new

            - method POST

            {
                to_user: int,
                comment: string

            }



    '''
    serializer_class = CommentSerializer
    permission_classes = []
    def post(self, request):
        print(request.data)
        serializers = self.serializer_class(data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response({'massage':'create at'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
