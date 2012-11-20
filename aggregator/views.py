import datetime

from django import utils
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_safe, require_GET
from django.views.decorators.gzip import gzip_page

from aggregator import feed_updater
# from aggregator.decorators import require_secret_handshake
from aggregator.models import Entry, Update, Feed

@gzip_page
@require_safe
def home(request):
    latest_entries = Entry.objects.all().order_by('-pub_date')[:50]
    return render_to_response('home.html',
        {'entries': latest_entries},
        context_instance=RequestContext(request)
    )

@gzip_page
@require_safe
def opml(request):
    return render_to_response('opml.xml',
        {'feeds': Feed.objects.all().order_by('id')},
        context_instance=RequestContext(request),
        mimetype="application/xml"
    )

@require_GET
# @require_secret_handshake
def update(request):
    latest_update = None
    try:
        latest_update = Update.objects.latest()
    except Update.DoesNotExist:
        pass

    if latest_update is None or (latest_update.timestamp <= (utils.timezone.now() - datetime.timedelta(hours=1))):
        response = StreamingHttpResponse(streaming_content=feed_updater.update_all(with_feedback=True),
            content_type='text/plain', status=200)
        if latest_update is not None:
            latest_update.timestamp = utils.timezone.now()
            latest_update.save()
        else:
            Update.objects.create(timestamp=utils.timezone.now())
    else:
        response = HttpResponse(content='Wat?', content_type='text/plain', status=200)

    return response
