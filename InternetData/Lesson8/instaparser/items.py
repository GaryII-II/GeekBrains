# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InstaparserPostsItem(scrapy.Item):
    # Posts related item
    user_id = scrapy.Field()
    username = scrapy.Field()
    photo = scrapy.Field()
    likes = scrapy.Field()
    post_data = scrapy.Field()


class InstaparserFollowersItem(scrapy.Item):
    # Followers related item
    userid = scrapy.Field()
    username = scrapy.Field()
    fullname = scrapy.Field()
    photo = scrapy.Field()
    following_id = scrapy.Field()
    follower_id = scrapy.Field()


