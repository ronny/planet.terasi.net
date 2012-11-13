# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.guid'
        db.add_column('aggregator_entry', 'guid',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=200),
                      keep_default=False)

        # Adding unique constraint on 'Entry', fields ['feed', 'guid']
        db.create_unique('aggregator_entry', ['feed_id', 'guid'])


    def backwards(self, orm):
        # Removing unique constraint on 'Entry', fields ['feed', 'guid']
        db.delete_unique('aggregator_entry', ['feed_id', 'guid'])

        # Deleting field 'Entry.guid'
        db.delete_column('aggregator_entry', 'guid')


    models = {
        'aggregator.entry': {
            'Meta': {'unique_together': "(('feed', 'guid'),)", 'object_name': 'Entry'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aggregator.Feed']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['aggregator']