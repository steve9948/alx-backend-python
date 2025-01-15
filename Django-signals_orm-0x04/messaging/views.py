from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .models import Message
from django.db.models import Prefetch

@login_required
def threaded_conversation(request, message_id):
    try:
        root_message = Message.objects.prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver').order_by('timestamp'))
        ).get(id=message_id)

        threaded_replies = root_message.fetch_threaded_replies()
        
        return render(request, 'messaging/threaded_conversation.html', {
            'root_message': root_message,
            'threaded_replies': threaded_replies
        })
    except Message.DoesNotExist:
        return HttpResponse("Message not found", status=404)

def delete_user(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            user.delete()
            messages.success(request, "Your account and all associated data have been deleted.")
            return redirect("/")  # Redirect to homepage or login page
        else:
            return HttpResponse("Unauthorized", status=401)
    return render(request, "messaging/delete_user.html")

@login_required
def unread_messages_view(request):
    unread_messages = Message.unread_messages.get_unread_messages(request.user)
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_messages})
