import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotescrawlItem


class QuoteLoginFormSpider(scrapy.Spider):

    name = "login-spider"
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def start_scraping(self, response):
        open_in_browser(response)
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

    def parse(self, response):
        # Get csrf_token
        csrf_token = response.css('form input::attr(value)').extract_first()
        # Login and return callback
        return FormRequest.from_response(response, formdata={
            'csrf_token': csrf_token,
            'username': "username",
            "password": "mypassword"
        }, callback=self.start_scraping)
