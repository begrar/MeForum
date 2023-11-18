from django.urls import path
from .views import UserRegsterView

urlpatterns = [
    path('register/', UserRegsterView.as_view(), name='register'),
]