from rest_framework import serializers
from ..models import Post
from user.serilizers import UserShortDetailSerializer
from categories.serializers import CategorySerializer
from postLikesDislikes.models import PostLikesDislikes



class PostSerializer(serializers.ModelSerializer):
    creator = UserShortDetailSerializer()
    category = CategorySerializer()
    likesCount = serializers.SerializerMethodField()
    dislikesCount = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'creator', 'publish_date', 'last_updated', 'category', 'views', 'image', 'video', 'gif', 'is_published','likesCount', 'dislikesCount']

    def get_likesCount(self, obj):
        return PostLikesDislikes.objects.filter(post=obj, type='like').count()

    def get_dislikesCount(self, obj):
        return PostLikesDislikes.objects.filter(post=obj, type='dislike').count()

class PostCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'image', 'video', 'gif')