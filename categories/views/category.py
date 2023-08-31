from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..models import Category
from ..serializers import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'parent_category']
    search_fields = ['name', 'description']
    ordering_fields = ['name']

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            return [IsAuthenticated(), IsAdminUser()]
        return super().get_permissions()

