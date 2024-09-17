from django.urls import path
from .views import custom_login_view

urlpatterns = [
    path('UserLogin/', custom_login_view, name='login'),
    # Add other URLs here
]
