# Books Crawler

Scarping Books from : http://books.toscrape.com/index.html

**1. pagination_spider**

-   Scrapes the book detail visiting each card's link in the paginated row items of books card.
-   **Run Spider:** `scrapy crawl paginated-books -o paginated-books.csv`
-   **Sample Output File:** `paginated-books.csv`
-   Max Depth of url visit: 2 (Book Detail Url in Card, Next Page URL)

**2. category_pagination_spider**

-   Grabs each category's(in the left nav menu) link and scrapes each book detail visiting each card's link in the page paginated by specific category of book.
-   **Run Spider:** `scrapy crawl category-paginated-books -o category-paginated-books.csv`
-   **Sample Output File:** `category-paginated-books.csv`
-   Max Depth of url visit: 3 (Category URL, Book's Detail URL, Next Page URL)

**3. CategoryAsArgumentPaginatedBooksDetailSpider**

-   Takes category as argument and check if category exists and scrapes the book with such category.
-   **Run Spider:** `scrapy crawl category-spider -a category=mystery -o mystery.csv`
-   **Sample Output File:** `mystery.csv`
-   Max Depth of url visit: 3 (Category URL, Book's Detail URL, Next Page URL)
