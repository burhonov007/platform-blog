from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostLikesDislikesViewSet

router = DefaultRouter()
router.register(r'', PostLikesDislikesViewSet, basename='post-likes-dislikes')

urlpatterns = [
    path('', include(router.urls)),
]
