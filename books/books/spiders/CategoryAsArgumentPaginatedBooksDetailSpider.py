import scrapy

from ..items import CategoeyPaginatedBooksDetailsItem

"""
scrapy crawl category-spider -a category=travel
scrapy crawl category-spider -a category=travel -L WARN
To know the log level:
"""


class CategoryAsArgumentPaginatedBooksDetailSpider(scrapy.Spider):
    """Takes category as argument and scrapes the details."""

    name = "category-spider"
    start_urls = ["http://books.toscrape.com/index.html"]

    def __init__(self, category=None, **kwargs):
        self.category_arg = category
        super().__init__(**kwargs)

    def parse(self, response):
        categories = response.css(".nav-list ul a")

        contains_category = False
        for item in categories:
            name = item.css("::text").extract_first().strip()
            link = item.css("::attr(href)").extract_first()

            if name.lower() == self.category_arg.lower():
                contains_category = True
                self.logger.warn('Category found')
                yield response.follow(link, self.parse_by_pagination, meta={'category': name})

        if not contains_category:
            self.logger.warn('No category found')

    def parse_by_pagination(self, response):
        book_cards = response.css("li.col-xs-6")
        for card in book_cards:
            detail_url = card.css(
                "article.product_pod a::attr(href)").extract_first()
            yield response.follow(detail_url, callback=self.parse_book_detail)

        next_url_count = response.css('li.next a::attr(href)')

        # Pagination
        if len(next_url_count) != 0:
            self.logger.warn("Switching Page Size using pagination")
            yield response.follow(next_url_count.extract_first(), callback=self.parse_by_pagination)

    def parse_book_detail(self, response):
        item = CategoeyPaginatedBooksDetailsItem()

        # Link of prev page and current page
        category = self.category_arg
        current_link = response.request.url

        # Books Info
        name = response.css("h1::text").extract_first()
        price = response.css(".price_color::text").extract_first()
        upc = response.css("tr:nth-child(1) td::text").extract_first()

        self.logger.warn(f"Parsed Book {name} from {current_link}")

        item['current_link'] = current_link

        item['category'] = category
        item['name'] = name
        item['price'] = price
        item['upc'] = upc
        yield item
