from rest_framework import serializers
from ..models import Comment
from user.serilizers import UserSerializer
from posts.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer() 
    post = PostSerializer()       
    class Meta:   
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'comment_date')
        

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Comment
        fields = ('text', 'post')
        