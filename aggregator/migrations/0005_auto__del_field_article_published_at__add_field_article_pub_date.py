# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.published_at'
        db.delete_column('aggregator_article', 'published_at')

        # Adding field 'Article.pub_date'
        db.add_column('aggregator_article', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 11, 7, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Article.published_at'
        db.add_column('aggregator_article', 'published_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Deleting field 'Article.pub_date'
        db.delete_column('aggregator_article', 'pub_date')


    models = {
        'aggregator.article': {
            'Meta': {'object_name': 'Article'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aggregator.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
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