from django.db import models


class Feed(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200, blank=True)

    site_url = models.URLField(blank=True)
    icon_url = models.URLField(blank=True)

    last_modified = models.DateTimeField(blank=True, null=True)
    etag = models.CharField(max_length=200, blank=True)
    last_fetched = models.DateTimeField(blank=True, null=True)

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
    authors = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "entries"
        unique_together = ('feed', 'guid',)
