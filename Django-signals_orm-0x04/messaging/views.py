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

@login_required
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

@login_required
def send_message(request):
    if request.method == "POST":
        content = request.POST.get("content")
        receiver_id = request.POST.get("receiver_id")
        if content and receiver_id:
            receiver = User.objects.get(id=receiver_id)
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            messages.success(request, "Message sent successfully.")
            return redirect("/messages/")  # Replace with the appropriate URL
    return render(request, "messaging/send_message.html")

@login_required
def message_list(request):
    messages = Message.objects.filter(receiver=request.user).only('id', 'sender', 'content', 'timestamp')
    return render(request, "messaging/message_list.html", {"messages": messages})

@login_required
def unread_for_user(request):
    unread_messages = Message.unread_messages.get_unread_messages(request.user)
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_messages})
