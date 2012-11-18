from django.contrib.syndication.views import Feed as SyndicationFeed
from django.utils.feedgenerator import Atom1Feed

from aggregator.models import Entry

class LatestEntriesFeed(SyndicationFeed):
    title = "Planet Terasi"
    link = "http://planet.terasi.net/"
    feed_url = "http://planet.terasi.net/feed/"
    description = "Think. Read. Write."

    def items(self):
        return Entry.objects.order_by('-pub_date')[:50]

    def item_guid(self, item):
        return item.guid

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return item.url

    def item_pubdate(self, item):
        return item.pub_date

    def item_author_name(self, item):
        return item.authors


class AtomLatestEntriesFeed(LatestEntriesFeed):
    feed_type = Atom1Feed
    subtitle = LatestEntriesFeed.description
