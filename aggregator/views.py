from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_safe
from django.views.decorators.gzip import gzip_page

from aggregator.models import Entry

@require_safe
@gzip_page
def home(request):
    latest_entries = Entry.objects.all().order_by('-pub_date')[:100]
    return render_to_response('home.html', {'entries': latest_entries})

@require_safe
def update(request):
    return HttpResponse("Wat?")
