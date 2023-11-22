from django.urls import path
from .views import UserRegsterView, UserEditView

urlpatterns = [
    path('register/', UserRegsterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]