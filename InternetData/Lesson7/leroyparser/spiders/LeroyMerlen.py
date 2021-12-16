import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from leroyparser.items import LeroyparserItem

class LeroymerlenSpider(scrapy.Spider):
    name = 'LeroyMerlen'
    allowed_domains = ['spb.leroymerlin.ru']

    def __init__(self, search, **kwargs):
        super().__init__(**kwargs)

        self.start_urls = ['https://spb.leroymerlin.ru/catalogue/stolyarnye-izdeliya/']

    def parse(self, response: HtmlResponse):
        links = response.xpath("//div[@data-qa-product]/a/@href")
        for link in links:
            yield response.follow(link, callback=self.parse_goods)

    def parse_goods(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroyparserItem(), response=response)
        loader.add_xpath('name', "//h1[@slot='title']/text()")
        loader.add_value('price', response.xpath("//meta[@itemprop='price']/@content").get())
        loader.add_value('link', response.url)
        loader.add_xpath('photos', "//img[@slot='thumbs']/@src")
        yield loader.load_item()
