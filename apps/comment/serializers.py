from rest_framework import serializers
from .models import Comment
from django.db.models import Q

from ..account.serializers import MainUserSerializer
from ..advertising.models import Advertising
from ..account.models import User

from ..advertising.serializers import AdminAdvertisingViewSerializer


class AdvertisingCommentsSerializer(AdminAdvertisingViewSerializer):
    class Meta:
        model = Advertising
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'is_active',
                  'diffusion',
                  )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('advertised', 'to_user', 'massage')

    def create(self, validated_data):
        user_id = self.context['request'].user
        advertised_id = validated_data.pop('advertised')
        comment = validated_data.pop('massage')
        to_user = validated_data['to_user']
        validate_advertise = Advertising.objects.filter(pk=advertised_id.id)
        if validate_advertise.exists():

            val = validate_advertise.first()
            if val.is_active:
                user_validate = val.user
                if user_validate == user_id:
                    raise serializers.ValidationError('comment not found')
        else:
            raise serializers.ValidationError('advertise')

        discussion_forum1 = Comment.objects.filter(
            Q(to_user=to_user.id, user=user_id, advertised_id=advertised_id.id) or
            Q(to_user=user_id, user=to_user.id, advertised_id=advertised_id.id))

        if comment in ['', None]:
            raise serializers.ValidationError('comment can not none')
        if discussion_forum1.exists():
            discussion_forum = discussion_forum1.first()

            parent = c if (
                c := Comment.objects.filter(discussion_forum=discussion_forum.discussion_forum).last()) else None
            return Comment.objects.create(user=user_id,
                                          advertised=advertised_id,
                                          massage=comment,
                                          to_user=to_user,
                                          parent=parent,
                                          discussion_forum=discussion_forum.discussion_forum)
        to_user = User.objects.filter(pk=to_user.id).first()
        discussion_forums = Comment.objects.all().values('discussion_forum')
        discussion = discussion_forums.last() if discussion_forums.exists() else {'discussion_forum': 0}
        return Comment.objects.create(user=user_id,
                                      to_user=to_user,
                                      massage=comment,
                                      advertised=advertised_id,
                                      parent=None,
                                      discussion_forum=discussion['discussion_forum'] + 1)


class UserSerializer(MainUserSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'is_kyc',
                  'image_Official_photo')


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id',
                  'user',
                  'to_user',
                  'massage',
                  'discussion_forum',
                  'parent')


class ReplayCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('massage',
                  'discussion_forum')

    def create(self, validated_data):
        discussion_forum = validated_data['discussion_forum']
        comment = Comment.objects.filter(discussion_forum=discussion_forum).last()
        if comment is None:
            raise serializers.ValidationError('discussion forum can not none')

        to_users = Comment.objects.filter(user=self.context['request'].user, discussion_forum=discussion_forum)
        if to_users.exists():
            validated_data['to_user'] = to_users.first().to_user
        else:
            to_users = Comment.objects.filter(to_user=self.context['request'].user,
                                              discussion_forum=discussion_forum)
            validated_data['to_user'] = to_users.first().user
        validated_data['parent'] = comment
        validated_data['user'] = self.context['request'].user
        validated_data['advertised'] = comment.advertised
        return Comment.objects.create(**validated_data)
