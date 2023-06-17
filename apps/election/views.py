from django.shortcuts import render, get_object_or_404
from .models import Election


def election_list(request):
    elections = Election.objects.all()
    return render(request, 'election_list.html', {'elections': elections})


def election_detail(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    return render(request, 'election_detail.html', {'election': election})
