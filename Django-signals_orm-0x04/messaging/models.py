from django.db import models
from django.contrib.auth.models import User

from messaging.managers import UnreadMessagesManager

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    edited_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='edited_messages')
    parent_message = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    read = models.BooleanField(default=False)

    objects = models.Manager()  # Default manager
    unread_messages = UnreadMessagesManager()  # Custom manager

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"

    def fetch_threaded_replies(self):
        """
        Recursive function to fetch all replies to this message in a threaded format.
        """
        replies = self.replies.all().select_related('sender', 'receiver')
        threaded_replies = []
        for reply in replies:
            threaded_replies.append({
                'message': reply,
                'replies': reply.fetch_threaded_replies()
            })
        return threaded_replies

class MessageHistory(models.Model):
    original_message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='edit_history')
    old_content = models.TextField()
    edit_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Edit history for message {self.original_message.id} at {self.edit_timestamp}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='notifications')
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} about message {self.message.id}"