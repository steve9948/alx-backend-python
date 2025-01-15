from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.contrib.auth.models import User
from django.utils.timezone import now

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Check if the message already exists (is being updated)
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                MessageHistory.objects.create(
                    original_message=old_message,
                    old_content=old_message.content
                )
                instance.edited = True
                instance.edited_at = now()
                # Assuming the user editing is stored in instance.edited_by
        except Message.DoesNotExist:
            pass

@receiver(post_delete, sender=User)
def clean_up_user_data(sender, instance, **kwargs):
    # Delete all messages sent or received by the user
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete all notifications for the user
    Notification.objects.filter(user=instance).delete()

    # Delete all message histories linked to the user's messages
    MessageHistory.objects.filter(original_message__sender=instance).delete()
    MessageHistory.objects.filter(original_message__receiver=instance).delete()

# messaging/apps.py
from django.apps import AppConfig

class MessagingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messaging'

    def ready(self):
        import messaging.signals