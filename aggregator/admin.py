from django.contrib import admin
from aggregator.models import Feed, Article

class FeedAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feed, FeedAdmin)

class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, ArticleAdmin)
