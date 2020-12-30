import scrapy

from ..items import PaginatedBooksDetailsItem

"""
Concepts Covered:
- Crawling paginated items
- Passing meta data from one level of link to nested links using meta.
"""

# Paginated book list url
pagination_base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Book details url
book_base_url = "http://books.toscrape.com/catalogue/{}"


class PaginatedBookDetailSpider(scrapy.Spider):
    """Redirect inside the links of books paginated and extracts book details"""

    start_urls = [pagination_base_url.format(1)]
    name = "paginated-books"

    def parse(self, response):
        book_cards = response.css("li.col-xs-6")
        for card in book_cards:
            detail_url = card.css(
                "article.product_pod a::attr(href)").extract_first()

            """meta is used to pass the data from the first link context to another link context"""
            yield scrapy.Request(book_base_url.format(detail_url), callback=self.parse_book_detail, meta={'parent_link': response.request.url})

        next_url_count = response.css('li.next a::attr(href)')

        # Pagination
        if len(next_url_count) != 0:
            next_page_number = response.css('li.next a::attr(href)').extract_first().split(".")[
                0].split("-")[-1]
            yield scrapy.Request(pagination_base_url.format(next_page_number), callback=self.parse)

    def parse_book_detail(self, response):
        item = PaginatedBooksDetailsItem()

        # Link of prev page and current page
        parent_link = response.meta['parent_link']
        current_link = response.request.url

        # Books Info
        name = response.css("h1::text").extract_first()
        price = response.css(".price_color::text").extract_first()
        upc = response.css("tr:nth-child(1) td::text").extract_first()

        item['parent_link'] = parent_link
        item['current_link'] = current_link

        item['name'] = name
        item['price'] = price
        item['upc'] = upc
        yield item
