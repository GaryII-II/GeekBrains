import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://spb.hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&search_field=description&fromSearchLine=true&text=python',
                  'https://spb.hh.ru/search/vacancy?area=2&search_field=name&search_field=company_name&search_field=description&fromSearchLine=true&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath('//a[@data-qa="pager-next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath('//a[@data-qa="vacancy-serp__vacancy-title"]/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath('//h1//text()').get()
        salary = response.xpath("//div[@class='vacancy-salary']//text()").getall()
        salary = [item.replace(u'\xa0', u'') for item in salary]
        link = response.url.split('?')[0]
        item = JobparserItem(name=name, salary=salary, link=link)
        yield item

