# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def clear_price(value):
    value = value.replace('\xa0', '')
    try:
        return int(value)
    except:
        return value


class LeroyparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(clear_price))
    price = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(clear_price))
    link = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
