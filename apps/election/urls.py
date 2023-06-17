from django.urls import path
from . import views

app_name = 'elections'

urlpatterns = [
    path('elections/', views.ElectionListView.as_view(), name='election_list'),
    path('<int:election_id>/', views.ElectionDetailView.as_view(), name='election_detail'),
]
