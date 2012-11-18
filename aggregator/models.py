import datetime

from django.db import models


class Update(models.Model):
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return "%s" % (self.timestamp,)

    class Meta:
        get_latest_by = 'timestamp'


class Feed(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, default='')

    site_url = models.URLField(blank=True, default='')
    icon_url = models.URLField(blank=True, default='')

    last_modified = models.DateTimeField(blank=True, null=True)
    etag = models.CharField(max_length=200, blank=True, default='')

    last_fetched = models.DateTimeField(blank=True, null=True)
    last_status = models.CharField(max_length=20, blank=True, default='')
    last_error = models.CharField(max_length=200, blank=True, default='')

    def __unicode__(self):
        if self.title is not None and self.title != "":
            return self.title
        else:
            return self.url


class Entry(models.Model):
    feed = models.ForeignKey(Feed)
    guid = models.CharField(max_length=200)
    url = models.URLField()
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200, blank=True, default='')
    content = models.TextField()
    content_type = models.CharField(max_length=200, default='text/plain')
    pub_date = models.DateTimeField()

    def __unicode__(self):
        if self.title is not None and self.title != "":
            return self.title
        else:
            return self.url

    class Meta:
        verbose_name_plural = "entries"
        # guid should be globally unique (hence the g in guid), but who knows about implementations eh, so
        # let's scope it by feed.
        unique_together = ('feed', 'guid',)
        get_latest_by = 'pub_date'
        ordering = ['-pub_date']
