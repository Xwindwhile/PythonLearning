# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeimageItem(scrapy.Item):
    title=scrapy.Field()
    img_url=scrapy.Field()
