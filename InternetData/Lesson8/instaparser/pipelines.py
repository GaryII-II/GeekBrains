# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# from itemadapter import ItemAdapter
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class InstaparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.instafollows

    def process_item(self, item, spider):

        collection_users = self.mongobase[spider.name]
        collection_follows = self.mongobase['follows']

        scrapy_item = item
        following_id = scrapy_item['following_id']
        follower_id = scrapy_item['follower_id']
        del scrapy_item['following_id']
        del scrapy_item['follower_id']
        scrapy_item['_id'] = hash(frozenset(scrapy_item.items()))

        # Add a user
        try:
            collection_users.insert_one(scrapy_item)
        except DuplicateKeyError as e:
            print(f'Duplicated record skipping: ' + scrapy_item['username'])

        # Add the following info to a separate table
        if following_id:
            follows = {"follower": scrapy_item["userid"], "following": following_id}
            collection_follows.insert_one(follows)
        elif follower_id:
            follows = {"follower": follower_id, "following": scrapy_item["userid"]}
            collection_follows.insert_one(follows)

        return scrapy_item
