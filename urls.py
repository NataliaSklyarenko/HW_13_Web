from django.urls import path
from . import views

urlpatterns = [
    # Інші URL-адреси вашого додатку...
    path('reset-password/', views.reset_password, name='reset_password'),
]