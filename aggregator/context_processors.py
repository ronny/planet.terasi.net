from aggregator.models import Feed, Update

def common(request):
    update = None
    try:
        update = Update.objects.latest()
    except Update.DoesNotExist:
        pass
    return {
        'feeds': Feed.objects.all().order_by('title'),
        'latest_update': update,
    }
