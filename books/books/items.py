# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaginatedBooksDetailsItem(scrapy.Item):
    parent_link = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    upc = scrapy.Field()
    current_link = scrapy.Field()
