from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['participants__username', 'participants__email']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        participants = self.request.data.get('participants')
        if not participants or len(participants) < 2:
            raise ValidationError("A conversation must have at least two participants.")
        serializer.save()

    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        conversation = self.get_object()
        messages = conversation.messages.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['message_body', 'sender__username']
    ordering_fields = ['sent_at']

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get('conversation')
        if not conversation:
            raise ValidationError("Conversation is required to send a message.")
        serializer.save()
