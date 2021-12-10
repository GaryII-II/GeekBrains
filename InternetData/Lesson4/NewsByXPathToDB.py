# https://gb.ru/lessons/184651/homework
# Read main news from sites  news.mail.ru, lenta.ru, yandex-новости with XPath and fill DB
# Add fields: source name, news title, link to the news, publication date

from lxml import html
import requests
from pprint import pprint

# Chrome
headers = {'Accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

# Edge
# headers = {'Accept': '*/*',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}


def get_news_mail_date_source(news_url):

    if not news_url:
        return None, None

    response = requests.get(news_url, headers=headers)
    if not response.ok:
        print(f'Request error: {response.status_code}')
        return

    dom = html.fromstring(response.text)

    # Get text of the page date/ago element
    news_date = dom.xpath("//span[@class='note__text breadcrumbs__text js-ago']/./@datetime")[0]
    news_source = dom.xpath("//a[@class='link color_gray breadcrumbs__link']//span[@class='link__text']/text()")[0]

    return news_date, news_source


# Get news from mail ru
def get_news_mail_ru():
    response = requests.get('https://news.mail.ru/', headers=headers)
    if not response.ok:
        print(f'Request error: {response.status_code}')
        return

    dom = html.fromstring(response.text)
    items = dom.xpath("//div[starts-with(@class,'daynews__item')]")

    news = []
    for item in items:
        news_item = {}

        news_title = item.xpath(".//span[starts-with(@class,'photo__title photo__title_new')]/text()")[0]
        news_link = item.xpath(".//a/@href")[0]

        # Get news date and source by a found news url
        news_date, news_source = get_news_mail_date_source(news_link)

        news_item['news_source'] = news_source
        news_item['news_title'] = news_title.replace(u'\xa0', u' ')
        news_item['news_link'] = news_link
        news_item['news_date'] = news_date

        news.append(news_item)

    pprint(news)

    return news


# Add news to DB
def fill_news_db(news_list):
    from pymongo import MongoClient
    from pymongo.errors import DuplicateKeyError

    # Connecting to Database to store the data
    client = MongoClient("127.0.0.1", 27017)
    db = client['NewsDB']
    news_collection = db.main_news

    # Insert to the collection
    added = 0
    for news in news_list:
        try:
            news_collection.insert_one(news)
            added = added + 1
        except DuplicateKeyError as e:
            print(f'Duplicated record found: ' + news['news_title'])

    print(f'\nAdded {added} news!\n')

    print(f'Read news from DB to check...\n')
    for job in news_collection.find({}):
        pprint(job)


# Process news.mail.ru
news_mail_ru = get_news_mail_ru()

# Fill Db with news
fill_news_db(news_mail_ru)

