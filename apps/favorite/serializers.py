from .models import Favorite
from rest_framework import serializers


class MainFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id',
                  'user',
                  'advertising'
                  )

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            user = self.context['request'].user
            advertising = validated_data['advertising']
            favorite = Favorite.objects.filter(user=user, advertising=advertising)
            if favorite.exists():
                favorite.delete()
            else:
                Favorite.objects.create(user=user, advertising=advertising)

            return validated_data
