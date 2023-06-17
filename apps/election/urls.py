from django.urls import path
from . import views

app_name = 'elections'

urlpatterns = [
    path('elections/', views.election_list, name='election_list'),
    path('<int:election_id>/', views.election_detail, name='election_detail'),
]
