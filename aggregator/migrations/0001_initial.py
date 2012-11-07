# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table('aggregator_feed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('icon_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('etag', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_fetched', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('aggregator', ['Feed'])

        # Adding model 'Article'
        db.create_table('aggregator_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aggregator.Feed'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('aggregator', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table('aggregator_feed')

        # Deleting model 'Article'
        db.delete_table('aggregator_article')


    models = {
        'aggregator.article': {
            'Meta': {'object_name': 'Article'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aggregator.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'aggregator.feed': {
            'Meta': {'object_name': 'Feed'},
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'icon_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_fetched': ('django.db.models.fields.DateTimeField', [], {}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['aggregator']