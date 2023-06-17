from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.accounts.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]