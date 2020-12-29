import scrapy

from ..items import QuotescrawlItem


class QuoteSpider(scrapy.Spider):
    """
        Docs: https://docs.scrapy.org/en/latest/topics/spiders.html
    """

    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # Instantiate the Itm Container
        items = QuotescrawlItem()

        # Parse the content
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
