import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class SuperjobSpider(scrapy.Spider):
    name = 'superjob'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://superjob.ru/vacancy/search/?keywords=python']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[contains(@class, 'f-test-link-Dalshe')]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//div[contains(@class, 'f-test-vacancy-item')]//a[contains(@href,'/vakansii/')]/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):

        name = response.xpath('//h1//text()').get()
        salary = response.xpath("//h1/following-sibling::span/span[1]/text()").extract()
        salary = [item.replace(u'\xa0', u'') for item in salary]
        link = response.url.split('?')[0]
        item = JobparserItem(name=name, salary=salary, link=link)
        yield item
