"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', include('categories.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/post-like-dislike/', include('postLikesDislikes.urls')),
    path('api/v1/posts/', include('posts.urls')),
    path('api/v1/', include('user.urls')),
]


# SWAGGER
if (settings.DEBUG):
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
    urlpatterns += [        
        path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/v1/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
    