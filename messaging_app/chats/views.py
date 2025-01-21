from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset to handle listing, retrieving, creating, and updating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=False, methods=["post"])
    def create_conversation(self, request):
        """
        Custom endpoint to create a new conversation.
        Expects a list of participant IDs in the payload.
        """
        participants = request.data.get("participants")
        if not participants or len(participants) < 2:
            return Response(
                {"error": "A conversation must have at least two participants."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Create the conversation
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        conversation.save()
        return Response(
            ConversationSerializer(conversation).data,
            status=status.HTTP_201_CREATED,
        )


class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset to handle listing, retrieving, creating, and updating messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        """
        Overrides the create method to handle sending a message to an existing conversation.
        """
        conversation_id = request.data.get("conversation_id")
        sender_id = request.data.get("sender")
        message_body = request.data.get("message_body")

        if not conversation_id or not sender_id or not message_body:
            return Response(
                {"error": "conversation_id, sender, and message_body are required fields."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        conversation = get_object_or_404(Conversation, pk=conversation_id)
        message = Message.objects.create(
            conversation=conversation,
            sender_id=sender_id,
            message_body=message_body,
        )
        return Response(
            MessageSerializer(message).data,
            status=status.HTTP_201_CREATED,
        )
