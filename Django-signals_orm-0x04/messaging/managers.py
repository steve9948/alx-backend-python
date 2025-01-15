from django.db import models

class UnreadMessagesManager(models.Manager):
    def get_unread_messages(self, user):
        return self.filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')
