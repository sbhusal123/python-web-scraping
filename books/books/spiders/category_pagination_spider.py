import scrapy

from ..items import CategoeyPaginatedBooksDetailsItem


# category base url
category_base_url = "http://books.toscrape.com/{}"

# Paginated book list url
pagination_base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Book details url
book_base_url = "http://books.toscrape.com/catalogue/{}"


class CategoryPaginatedBookDetailSpider(scrapy.Spider):
    """Redirect inside the links of books paginated and extracts book details"""

    start_urls = ["http://books.toscrape.com/index.html"]
    name = "category-paginated-books"

    def parse(self, response):
        categories = response.css(".nav-list ul a")

        # Iterate through categories
        for item in categories:
            name = item.css("::text").extract_first().strip()
            link = item.css("::attr(href)").extract_first()
            yield scrapy.Request(category_base_url.format(link), self.parse_by_pagination, meta={'category': name})

    def parse_by_pagination(self, response):
        category = response.meta['category']
        book_cards = response.css("li.col-xs-6")
        for card in book_cards:
            detail_url = card.css(
                "article.product_pod a::attr(href)").extract_first()

            """meta is used to pass the data from the first link context to another link context"""
            yield response.follow(detail_url, callback=self.parse_book_detail, meta={'category': category})

        next_url_count = response.css('li.next a::attr(href)')

        # Pagination
        if len(next_url_count) != 0:
            yield response.follow(next_url_count.extract_first(), callback=self.parse_by_pagination, meta={'category': category})

    def parse_book_detail(self, response):
        item = CategoeyPaginatedBooksDetailsItem()

        # Link of prev page and current page
        category = response.meta['category']
        current_link = response.request.url

        # Books Info
        name = response.css("h1::text").extract_first()
        price = response.css(".price_color::text").extract_first()
        upc = response.css("tr:nth-child(1) td::text").extract_first()

        item['current_link'] = current_link

        item['category'] = category
        item['name'] = name
        item['price'] = price
        item['upc'] = upc
        yield item
