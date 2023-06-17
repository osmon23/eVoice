from django.urls import path
from .views import WorkerLoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', WorkerLoginView.as_view(), name='login'),
]
