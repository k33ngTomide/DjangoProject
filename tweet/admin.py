from django.contrib import admin

import user
from tweet.models import Tweet, Comment


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['text', 'last_update']
    list_per_page = 15
    search_fields = ['text']
    list_display_links = ['text']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'commented_on', 'tweet', 'id']


# Register your models here.
# admin.site.register(Tweet)
