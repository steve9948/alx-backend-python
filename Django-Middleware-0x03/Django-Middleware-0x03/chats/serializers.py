from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # Nested UserSerializer to show sender details
    sender_name = serializers.SerializerMethodField()  # Custom field for the sender's name

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_name', 'conversation', 'message_body', 'sent_at']

    def get_sender_name(self, obj):
        # Custom method to get sender's full name
        return f"{obj.sender.first_name} {obj.sender.last_name}"

    def validate_message_body(self, value):
        # Custom validation to ensure the message body isn't too short
        if len(value) < 5:
            raise serializers.ValidationError("Message body must be at least 5 characters long.")
        return value

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)  # Nested UserSerializer for participants
    messages = MessageSerializer(many=True, read_only=True, source='messages')  # Nested MessageSerializer
    conversation_title = serializers.CharField(source='__str__', read_only=True)  # Custom field for conversation title

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages', 'conversation_title']

    def validate(self, data):
        # Custom validation to ensure there are at least two participants in a conversation
        if len(data['participants']) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")
        return data
