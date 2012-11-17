from django.contrib import admin
from aggregator.models import Feed, Entry

class FeedAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'site_url', 'last_status')
    list_filter = ('last_status',)
admin.site.register(Feed, FeedAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'feed')
    list_filter = ('feed',)
admin.site.register(Entry, EntryAdmin)
