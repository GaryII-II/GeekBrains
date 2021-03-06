# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import scrapy
# from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class LeroyparserPipeline:
    def process_item(self, item, spider):
        print()
        return item

class LeroyPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

    # Distributes downloading images to folders with the names obtained from the 1st word of the name. It acts like a category of goods
    def file_path(self, request, response=None, info=None, *, item=None):
        current_name = list(info.downloading)[0]
        return f"{item['name'].split(' ')[0]}/{current_name}.jpg"
