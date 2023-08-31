from rest_framework import serializers
from ..models import PostLikesDislikes
from user.serilizers import UserShortDetailSerializer
from posts.serializers import PostSerializer

class PostLikeDislikeSerializer(serializers.ModelSerializer):
    user = UserShortDetailSerializer()
    post = PostSerializer()
    class Meta:
        model = PostLikesDislikes
        fields = ('id', 'user', 'post', 'type', 'date')


class PostLikeDislikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikesDislikes
        fields = ('post', 'type')
