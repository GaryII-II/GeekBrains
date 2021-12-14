# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# TASK: https://gb.ru/lessons/184653/homework

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class JobparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacancy0712

    def process_item(self, item, spider):

        if spider.name == 'superjob':
            item['min'], item['max'], item['cur'] = self.process_salary_sj(item['salary'])
        elif spider.name == 'Hhru':
            item['min'], item['max'], item['cur'] = self.process_salary_hh(item['salary'])
        else:
            item['min'] = None
            item['max'] = None
            item['cur'] = None

        del item['salary']

        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item

    def get_salary_bound_hh(self, salary, bound_type):
        res = None
        try:
            index = salary.index(bound_type)
            val = salary[index + 1]
            if val.isdigit():
                res = int(salary[index+1])
            else:
                res = salary[index+1]
        except ValueError:
            res = None

        return res

    def process_salary_hh(self, salary):

        min, max, cur = None, None, None
        # When the salary was not declared
        if not salary or len(salary) <= 1:
            return min, max, cur

        min = self.get_salary_bound_hh(salary, 'от ')
        max = self.get_salary_bound_hh(salary, ' до ')
        cur = self.get_salary_bound_hh(salary, ' ')

        return min, max, cur

    def process_salary_sj(self, salary):

        min, max, cur = None, None, None
        # When the salary was not declared
        if not salary or len(salary) <= 1:
            return min, max, cur

        length = len(salary)
        if length == 3:
            import re

            number = ''.join(re.findall('[0-9]', salary[2]))
            cur = ''.join(re.findall('\D', salary[2]))

            if salary[0] == u'от':
                min = int(number)
            elif salary[0] == u'до':
                max = int(number)
        elif length == 4:
            min = int(salary[0])
            max = int(salary[1])
            cur = salary[3]

        return min, max, cur