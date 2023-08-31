from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from ..models import PostLikesDislikes
from ..serializers import PostLikeDislikeSerializer, PostLikeDislikeCreateSerializer

class PostLikesDislikesViewSet(generics.ListAPIView,
                               generics.CreateAPIView,
                               generics.RetrieveAPIView,
                               viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = PostLikeDislikeSerializer

    def get_serializer_class(self):
        # Используйте разные сериализаторы в зависимости от действия
        if self.action in ['create']:
            return PostLikeDislikeCreateSerializer
        return PostLikeDislikeSerializer
    
    def get_queryset(self):
        user = self.request.user
        return PostLikesDislikes.objects.filter(user=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.validated_data['post']
        existing_like = PostLikesDislikes.objects.filter(user=user, post=post).first()

        if existing_like:
            if existing_like.type == serializer.validated_data['type']:
                existing_like.delete()
            else:
                existing_like.type = serializer.validated_data['type']
                existing_like.save()
        else:
            serializer.save(user=user)


