from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

# from instaparser.spiders.instagram_posts import InstaPostsSpider
from instaparser.spiders.instagram_follows import InstaFollowsSpider
from instaparser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
#    process.crawl(InstaPostsSpider)
    process.crawl(InstaFollowsSpider)

    process.start()