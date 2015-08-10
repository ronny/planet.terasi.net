# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(default=b'', max_length=200, blank=True)),
                ('content', models.TextField()),
                ('content_type', models.CharField(default=b'text/plain', max_length=200)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(default=b'', max_length=200, blank=True)),
                ('site_url', models.URLField(default=b'', blank=True)),
                ('icon_url', models.URLField(default=b'', blank=True)),
                ('last_modified', models.DateTimeField(null=True, blank=True)),
                ('etag', models.CharField(default=b'', max_length=200, blank=True)),
                ('last_fetched', models.DateTimeField(null=True, blank=True)),
                ('last_status', models.CharField(default=b'', max_length=20, blank=True)),
                ('last_error', models.CharField(default=b'', max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'get_latest_by': 'timestamp',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='feed',
            field=models.ForeignKey(to='aggregator.Feed'),
        ),
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together=set([('feed', 'guid')]),
        ),
    ]
