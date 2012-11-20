import datetime
import django
import logging
import feedparser
import time

from aggregator.models import Feed, Entry

feedparser.USER_AGENT = "Planet Terasi/3.0 +http://planet.terasi.net/"
logger = logging.getLogger(__name__)

def update_all(with_feedback=False):
    start = datetime.datetime.now()
    logger.info("update_all: started %s", start)
    success = failed = 0
    for feed in Feed.objects.all().order_by('id'):
        try:
            if with_feedback:
                yield "%s - %s\n" % (datetime.datetime.now(), feed.url,)
            update(feed)
            success += 1
        except Exception as e:
            failed += 1
            logger.warn("Exception while updating feed %s: %s", feed.url, e)
            feed.last_error = e
            feed.save()
            raise
    finish = datetime.datetime.now()
    logger.info("update_all: finished %s - %s, success=%d, failed=%d", finish, (finish - start), success, failed)


def update(feed):
    logger.info("updating feed %s", feed.url)
    parsed = feedparser.parse(
        feed.url,
        etag=feed.etag,
        modified=feed.last_modified,
    )
    logger.debug("status %s", parsed.get('status', None))

    __update_feed_attributes(feed, parsed)
    if parsed.get('status', None) == 200:
        __update_entries(feed, parsed)

#############################################################################

# https://docs.djangoproject.com/en/dev/topics/i18n/timezones/
import warnings
warnings.filterwarnings(
        'error', r"DateTimeField received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

def __update_feed_attributes(feed, parsed):
    if feed.title is None or feed.title == '':
        feed.title = parsed.feed.get('title', '')
    if feed.site_url is None or feed.site_url == '':
        feed.site_url = parsed.feed.get('link', '')
    if feed.icon_url is None or feed.icon_url == '':
        feed.icon_url = parsed.feed.get('icon', '')
    # Save both etag and last modified so that we can use them on future updates.
    # http://packages.python.org/feedparser/http-etag.html
    feed.etag = parsed.get('etag', '')
    feed.last_modified = __datetime(parsed.get('modified_parsed', None))
    feed.last_fetched = django.utils.timezone.now()
    feed.last_status = parsed.get('status', '')
    if feed.last_status in [301, 302, '301', '302']:
        href = parsed.get('href', None)
        if href is not None:
            logger.info("Updating feed url from %s to %s", feed.url, href)
            feed.url = href
    feed.save()

def __update_entries(feed, parsed):
    logger.info("%s: %d entries", feed.url, len(parsed.entries))
    for parsed_entry in parsed.entries:
        __update_entry(feed, parsed_entry)

def __update_entry(feed, parsed_entry):
    attributes = {
        'url': parsed_entry.get('link', None),
        'title': parsed_entry.get('title', None),
        'authors': __author(parsed_entry),
        'content': __content(parsed_entry).get('value', ''),
        'content_type': __content(parsed_entry).get('type', 'text/plain'),
        'pub_date': __datetime(parsed_entry.get('published_parsed', None)) or django.utils.timezone.now(),
    }
    logger.debug("__update_entry: attributes=%s", attributes)
    entry, created = Entry.objects.get_or_create(feed=feed, guid=__guid(parsed_entry), defaults=attributes)
    new = "new" if created else "existing"
    logger.info("entry: (%s) %s", new, entry.url)

def __content(parsed_entry):
    return parsed_entry.get('content', [{}])[0]

def __guid(parsed_entry):
    return parsed_entry.get('id', parsed_entry.get('link', None))

def __author(parsed_entry):
    author = ''
    author_detail = parsed_entry.get('author_detail', None)
    if author_detail is not None:
        author = author_detail.get('name', '')
    if author == '':
        author = parsed_entry.get('author', '')
    return author

def __datetime(struct_time):
    if struct_time is None:
        return None
    logger.debug("__datetime: struct_time=%s", struct_time)
    # Assume struct_time is UTC (which actually is for feedparser parsed datetimes).
    # http://packages.python.org/feedparser/date-parsing.html#supporting-additional-date-formats
    naive = datetime.datetime.fromtimestamp(time.mktime(struct_time))
    return naive.replace(tzinfo=django.utils.timezone.utc)


if __name__ == '__main__':
    update_all()
