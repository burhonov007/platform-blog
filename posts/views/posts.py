from rest_framework.permissions import IsAdminUser
from rest_framework import generics, viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from user.permission import IsModeratorUser
from ..serializers import PostCreateSerializer, PostSerializer
from ..models import Post
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class PostListViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class=PostSerializer
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(creator=user)
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'views', 'is_published', 'creator']
    ordering_fields = ['views', 'publish_date', 'last_updated']
    search_fields = ['title', 'content']  
    

class PostViewSet(generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.UpdateAPIView,
                  generics.RetrieveAPIView,
                  generics.DestroyAPIView, 
                  viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PostCreateSerializer
        return PostSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(creator=user)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        
    def perform_update(self, serializer):
        post = self.get_object()
        user = self.request.user
        
        if post.creator == user:
            serializer.save()
        else:
            return Response({'detail': 'You do not have permission to perform this action.'},
                            status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        user = self.request.user
        
        if instance.creator == user:        
            instance.delete()
        else:
            return Response({'detail': 'You do not have permission to perform this action.'},
                            status=status.HTTP_403_FORBIDDEN)

