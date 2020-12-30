import scrapy
import json

from ..items import QuotescrawlItem

"""
Scrapes the json data from the website that loads data on scrolling using ajax.
First of all inspect the data and url from the network.
"""
base_url = "http://quotes.toscrape.com/api/quotes?page={page_number}"


class ScrollSpider(scrapy.Spider):
    name = 'scroll'
    start_urls = [base_url.format(page_number=1)]

    def parse(self, response):
        data = json.loads(response.text)
        item = QuotescrawlItem()
        for quote in data["quotes"]:
            item['author'] = quote["author"]["name"]
            item['tag'] = quote["tags"]
            item['title'] = quote['text']
            yield item

        if data["has_next"]:
            current_page_no = response.request.url.split("=")[-1]
            next_page = int(current_page_no) + 1
            yield scrapy.Request(base_url.format(page_number=next_page), callback=self.parse)
