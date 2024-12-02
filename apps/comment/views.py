from django.shortcuts import render
from apps.account.models import User
from apps.advertising.models import Advertising
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer, CommentListSerializer, ReplayCommentSerializer

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
        serializers = self.serializer_class(data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response({'massage': 'create at'}, status=status.HTTP_200_OK)
        return Response({'error': serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class CommentDiscussionForumListView(APIView):
    def get(self, request):
        user = request.user.id
        comments = set(Comment.objects.filter(Q(user_id=user) | Q(to_user_id=user)).order_by(
            'discussion_forum').values_list('advertised_id', 'advertised__title', 'discussion_forum'))
        return Response({'comments': comments}, status=status.HTTP_200_OK)


class CommentListView(APIView):
    def post(self, request):
        discussion_form = request.data['discussion']
        comments = Comment.objects.filter(discussion_forum=int(discussion_form)).order_by(
            'created_at')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReplayToCommentView(APIView):
    def post(self, request):
        serializer = ReplayCommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'accepted'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
