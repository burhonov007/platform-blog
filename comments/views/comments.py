from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, filters
from ..models import Comment
from ..serializers import CommentSerializer, CommentCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['post']  
    search_fields = ['text']
    ordering_fields = ['comment_date'] 
    
    def get_serializer_class(self):
        if self.action in ['create'] or ['updade'] or ['partial_update']:
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            return [IsAuthenticated(), IsAdminUser()]
        return super().get_permissions()
