import feedparser
import logging

from aggregator.models import Feed

feedparser.USER_AGENT = "Planet Terasi/3.0 +http://planet.terasi.net/"
logger = logging.getLogger(__name__)

def update_all():
    for feed in Feed.objects.all():
        update(feed)

def update(feed):
    logger.debug("updating feed %s", feed.url)
    parsed = feedparser.parse(feed.url,
            etag=feed.etag,
            modified=feed.last_modified,
        )
    logger.debug("status %s", parsed.status)

    __update_feed_attributes(feed, parsed)
    __update_entries(feed, parsed)

#############################################################################

def __update_feed_attributes(feed, parsed):
    if feed.title is None or feed.title == "":
        feed.title = parsed.feed.title
    if feed.site_url is None or feed.site_url == "":
        feed.site_url = parsed.feed.link
    feed.last_modified = parsed.published_parsed

def __update_entries(feed, parsed):
    for parsed_entry in parsed.entries:
        __update_entry(feed, parsed_entry)

def __update_entry(feed, parsed_entry):
    entry, created = Entry.objects.get_or_create(feed=feed, guid=__guid(parsed_entry),
        defaults={
            'url': parsed_entry.url,
            'title': parsed_entry.title,
            'authors': parsed_entry.authors,
            'content': parsed_entry.description,
        })
    obj, created = Person.objects.get_or_create(first_name='John', last_name='Lennon',
                     defaults={'birthday': date(1940, 10, 9)})

    entry.title = parsed_entry.title

def __guid(parsed_entry):
    if parsed_entry.id is None or parsed_entry.id == "":
        return parsed_entry.link
    else:
        return parsed_entry.id
