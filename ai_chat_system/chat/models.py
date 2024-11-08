# chat/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    tokens = models.IntegerField(default=4000)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} at {self.timestamp}"
