from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

# Instantiate DefaultRouter
router = DefaultRouter()

# Register viewsets with the router
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Include the router-generated URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include all API routes from the router
]
