from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

# Instantiate DefaultRouter
routers = DefaultRouter()

# Register viewsets with the router
routers.register(r'conversations', ConversationViewSet, basename='conversation')
routers.register(r'messages', MessageViewSet, basename='message')

# Include the router-generated URLs in the urlpatterns
urlpatterns = [
    path('', include(routers.urls)),  # Include all API routes from the router
]
