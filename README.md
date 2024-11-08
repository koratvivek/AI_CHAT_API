# AI Chat System with Django

This is a Django-based AI chat system that allows users to register, log in, and interact with an AI-powered chatbot. Users are assigned tokens, which are deducted for each message sent to the chatbot.

## Features
- User registration and login
- Chat with an AI-powered chatbot
- Token deduction for each chat interaction
- Check token balance
- Logout functionality

## Requirements
- Python 3.x
- Django
- Django REST Framework

- Sample Input and Output
Sample 1: User Registration
Input
Username: testuser
Password: testpass
Output
Copy code
Registration successful.
Sample 2: User Login
Input
Username: testuser
Password: testpass
Output
Copy code
Login successful.
Sample 3: Chat Interaction
Input
Message: Hello AI, how are you?
Output
vbnet
Copy code
User: Hello AI, how are you?
AI: This is a dummy AI response to your message.

Remaining Tokens: 3900
Sample 4: Insufficient Tokens
Input
Message: Tell me a joke!
Output
vbnet
Copy code
Error: Insufficient tokens. You need at least 100 tokens to chat.
Sample 5: Checking Token Balance
Input
Authentication Token: abcdef12345
Output
yaml
Copy code
Remaining Tokens: 3900
