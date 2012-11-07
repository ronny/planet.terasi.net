# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feed.last_fetched'
        db.alter_column('aggregator_feed', 'last_fetched', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Feed.last_modified'
        db.alter_column('aggregator_feed', 'last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Feed.last_fetched'
        db.alter_column('aggregator_feed', 'last_fetched', self.gf('django.db.models.fields.DateTimeField')(default=None))

        # Changing field 'Feed.last_modified'
        db.alter_column('aggregator_feed', 'last_modified', self.gf('django.db.models.fields.DateTimeField')(default=None))

    models = {
        'aggregator.article': {
            'Meta': {'object_name': 'Article'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aggregator.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'aggregator.feed': {
            'Meta': {'object_name': 'Feed'},
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'icon_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['aggregator']