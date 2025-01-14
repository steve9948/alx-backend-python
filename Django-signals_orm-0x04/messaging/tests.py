from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from messaging.models import Message

class UnreadMessagesManagerTest(TestCase):
    def setUp(self):
        # Create two users
        self.sender = User.objects.create_user(username="sender", password="password")
        self.receiver = User.objects.create_user(username="receiver", password="password")

        # Create messages
        Message.objects.create(sender=self.sender, receiver=self.receiver, content="Message 1", read=False)
        Message.objects.create(sender=self.sender, receiver=self.receiver, content="Message 2", read=False)
        Message.objects.create(sender=self.sender, receiver=self.receiver, content="Message 3", read=True)

    def test_unread_messages(self):
        # Get unread messages for the receiver
        unread_messages = Message.unread_messages.get_unread_messages(self.receiver)

        # Assert that only unread messages are returned
        self.assertEqual(unread_messages.count(), 2)
        self.assertTrue(all(message.read is False for message in unread_messages))

    def test_no_unread_messages(self):
        # Mark all messages as read
        Message.objects.filter(receiver=self.receiver).update(read=True)

        # Get unread messages for the receiver
        unread_messages = Message.unread_messages.get_unread_messages(self.receiver)

        # Assert that no unread messages are returned
        self.assertEqual(unread_messages.count(), 0)