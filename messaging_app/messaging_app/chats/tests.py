from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Conversation, Message

class ConversationTests(APITestCase):
    def test_create_conversation(self):
        user1 = User.objects.create_user(username="user1", password="password")
        user2 = User.objects.create_user(username="user2", password="password")
        response = self.client.post('/conversations/', {"participants": [user1.id, user2.id]})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class MessageTests(APITestCase):
    def test_send_message(self):
        user1 = User.objects.create_user(username="user1", password="password")
        user2 = User.objects.create_user(username="user2", password="password")
        conversation = Conversation.objects.create()
        conversation.participants.set([user1, user2])
        response = self.client.post(f'/messages/{conversation.id}/send_message/', {
            "sender": user1.id,
            "content": "Hello!"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
