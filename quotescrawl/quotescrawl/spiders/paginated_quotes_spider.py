import scrapy

from ..items import QuotescrawlItem


class MultiPageQuoteSpider(scrapy.Spider):
    """
        Docs: https://docs.scrapy.org/en/latest/topics/spiders.html
    """

    name = "paginated-quotes-spider"
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

        # Crawl Next Page
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # response.follow(page, callback)
            yield response.follow(next_page, callback=self.parse)
