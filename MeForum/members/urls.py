from django.urls import path
from .views import UserRegsterView, UserEditView, PasswordsChangeView
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegsterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success', views.password_success, name="password_success"),
    
]
