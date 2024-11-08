from django.urls import path
from .views import register_view, login_view, chat_view, tokens_view, logout_view

urlpatterns = [
    #  path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('chat/', chat_view, name='chat'),
    path('tokens/', tokens_view, name='tokens'),
    path('logout/', logout_view, name='logout'),
]
