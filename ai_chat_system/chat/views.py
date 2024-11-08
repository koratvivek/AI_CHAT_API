from .models import Chat, User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .models import User, Chat
from django.contrib.auth.decorators import login_required

# Registration View


# def home_view(request):
#     return render(request, 'chat/home.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'chat/register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'chat/register.html')


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return redirect('chat')
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})
    return render(request, 'chat/login.html')


def logout_view(request):
    """Logs the user out and redirects to the login page."""
    logout(request)
    return redirect('login')


@login_required
def chat_view(request):
    try:
        # Fetch the authentication token and user's token balance
        auth_token = Token.objects.get(user=request.user).key
        user = request.user
        user_tokens = user.tokens

        # Handle POST request for sending a message
        if request.method == 'POST':
            message = request.POST.get('message')

            # Check if the user has enough tokens (100 tokens per message)
            if user_tokens < 500:
                return render(request, 'chat/chat.html', {
                    'error': 'Insufficient tokens. You need at least 100 tokens to chat.',
                    'chats': Chat.objects.filter(user=user).order_by('timestamp'),
                    'token': auth_token,
                    'user_tokens': user_tokens
                })

            # Deduct 100 tokens
            user.tokens -= 500
            user.save()

            # Generate a dummy AI response
            response = "This is a dummy AI response to your message."

            # Save the chat to the database
            Chat.objects.create(
                user=user,
                message=message,
                response=response,
                timestamp=timezone.now()
            )

        # Fetch all chat messages for the current user
        chats = Chat.objects.filter(user=user).order_by('timestamp')

        return render(request, 'chat/chat.html', {
            'chats': chats,
            'token': auth_token,
            'user_tokens': user.tokens
        })

    except Token.DoesNotExist:
        # Handle case where the token doesn't exist (edge case)
        return redirect('login')

# Token Balance View


@login_required
def tokens_view(request):
    user = request.user
    tokens = user.tokens
    return render(request, 'chat/tokens.html', {'tokens': tokens})
