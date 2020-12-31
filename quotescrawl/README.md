# Quotes Scraper

Scarping Quotes from : http://quotes.toscrape.com/

## Spiders(/quotescrawl/spiders/)

**1. login_spider.py:**

-   [Login Form URL](http://quotes.toscrape.com/login)
-   Logins to the site using username, password and csrf_token parsed from the response.
-   **Run Spider:** `scrapy crawl login-spider -o login-spider.csv`
-   **Sample Output File:** `login-spider.csv`

**2. paginated_quotes_spider.py**

-   [Paginated Quotes URL](http://quotes.toscrape.com/)
-   Extracts the quotes details from the paginated list of quotes show in cards.
-   **Run Spider:** `scrapy crawl paginated-quotes-spider -o paginated-quotes-spider.csv`
-   **Sample Output File:** `paginated-quotes-spider.csv`

**3. scroll_spider.py**

-   [Scrollable Quotes URL](http://quotes.toscrape.com/scroll)
-   Extracts the books details consuming the json response of api that are triggered when page is scrolled.
-   **Run Spider:** `scrapy crawl scroll-quotes-spider -o scroll-quotes-spider.csv`
-   **Sample Output File:** `scroll-quotes-spider.csv`

## Pipeline(/quotescrawl/pipeline.py)

**1. QuotescrawlPipeline**

-   Stores the quotes details in SQLite Database.
