from django.db import models


class Feed(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)

    icon_url = models.URLField(blank=True)

    last_modified = models.DateTimeField(blank=True, null=True)
    etag = models.CharField(max_length=200, blank=True)
    last_fetched = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    feed = models.ForeignKey(Feed)
    url = models.URLField()
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    published_at = models.DateTimeField()
