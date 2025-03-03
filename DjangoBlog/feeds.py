#!/usr/bin/env python
# encoding: utf-8


from django.contrib.syndication.views import Feed
from blog.models import Article
from django.conf import settings
from django.utils.feedgenerator import Rss201rev2Feed
from DjangoBlog.utils import CommonMarkdown
from django.contrib.auth import get_user_model
from datetime import datetime


class DjangoBlogFeed(Feed):
    feed_type = Rss201rev2Feed

    description = 'Feeds'
    title = "Let's listen to the wind yin."
    link = "/feed/"

    def author_name(self):
        return get_user_model().objects.first().nickname

    def author_link(self):
        return get_user_model().objects.first().get_absolute_url()

    def items(self):
        return Article.objects.filter(type='a', status='p').order_by('-pub_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return CommonMarkdown.get_markdown(item.body)

    def feed_copyright(self):
        now = datetime.now()
        return "Copyright© {year} Listen to the wind".format(year=now.year)

    def item_link(self, item):
        return item.get_absolute_url()

    def item_guid(self, item):
        return
