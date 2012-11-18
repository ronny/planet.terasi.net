from aggregator.models import Feed, Update

def common(request):
    return {
        'feeds': Feed.objects.all().order_by('title'),
        'latest_update': Update.objects.latest(),
    }
