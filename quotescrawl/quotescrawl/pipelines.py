# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
Enabling Pipeline
    - Add pipeline to the setting's ITEM_PIPELINES with priority as a number

How does it works:
    - After crawling the item, the items are returned to the pipline as per the priority
    - Then process the items i.e storing to the database
"""


class QuotescrawlPipeline:
    def process_item(self, item, spider):
        print("Pipeline: " + item['title'][0])
        print(item)
        return item
