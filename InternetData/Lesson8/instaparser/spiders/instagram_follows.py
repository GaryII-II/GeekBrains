import scrapy
import re
import json
from scrapy.http import HtmlResponse
from urllib.parse import urlencode
from instaparser.items import InstaparserFollowersItem
from instaparser.items import InstaparserPostsItem
from copy import deepcopy
from scrapy.shell import inspect_response

# Scrapping Instagram user posts
class InstaFollowsSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com/']
    inst_login_link = '	https://www.instagram.com/accounts/login/ajax/'
    # inst_login = 'Onliskill_udm'
    inst_login = 'garylltor'
    # inst_pwd = '#PWD_INSTAGRAM_BROWSER:10:1638551736:AedQAFI0vAAYTOunJJUOmrJPoJO3A6MjtJf+QOH/3ovuYhh9eIlQNGUh2MDiWMtQL80BL3LJqk7DfHobv+o7STw2Qg6qLwcDSuHFLa+tiYoPvNwdkG6zno3Y6Pr/Et12HLssUesjh66gbKA/Regr'
    inst_pwd = '#PWD_INSTAGRAM_BROWSER:10:1640707672:ASpQAP72OpGiesrPrDWsFgIoxUK70VbJvOLSMB1cnPxOo+MnIs+u1g/8H+BZ6/+v2pJqzsn9OcYGzt3MJOMFcFZ549vhPMdZEm+nu+esnVaX3dY8dxLUxe4RulwQmCTxaBTx/xRZS6dEp8VLHU188PY='
    users = ['ai_machine_learning', 'cyberpayload', 'born2peace']
    inst_graphql_link = 'https://i.instagram.com/api/v1/friendships/'
    limit_users = 1

    def parse(self, response: HtmlResponse):
        csrf = self.fetch_csrf_token(response.text)
        yield scrapy.FormRequest(self.inst_login_link,
                                 method='POST',
                                 callback=self.login,
                                 formdata={'username': self.inst_login,
                                           'enc_password': self.inst_pwd},
                                 headers={'X-CSRFToken': csrf})

    def login(self, response: HtmlResponse):
        j_data = response.json()
        if j_data.get('authenticated'):
            for user in self.users:
                yield response.follow(
                    f'/{user}',
                    callback=self.user_parse,
                    cb_kwargs={'username': user}
                )

    # Scan followers
    def user_parse(self, response: HtmlResponse, username):
        user_id = self.fetch_user_id(response.text, username)
        variables = {'count': 12, 'search_surface': 'follow_list_page'}
        url_followers = f'{self.inst_graphql_link}{user_id}/followers/?{urlencode(variables)}'

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # THIS REQUEST ALWAYS RETURNS 400 CODE and STOPS SCRAPPING. I GOT STUCK HERE
        yield response.follow(
            url_followers,
            callback=self.user_followers_parse,
            cb_kwargs={'username': username,
                       'user_id': user_id,
                       'variables': deepcopy(variables)}
        )

        variables = {'count': 12}
        url_following = f'{self.inst_graphql_link}{user_id}/following/?{urlencode(variables)}'

        yield response.follow(
            url_following,
            callback=self.user_following_parse,
            cb_kwargs={'username': username,
                       'user_id': user_id,
                       'variables': deepcopy(variables)}
        )

    def user_followers_parse(self, response: HtmlResponse, username, user_id, variables):
        j_data = response.json()
        followers_info = j_data.get('users')
        max_id = j_data.get('next_max_id')
        if max_id:
            variables['max_id'] = max_id
            url_followers = f'{self.inst_graphql_link}{user_id}/followers/?{urlencode(variables)}'

            yield response.follow(
                url_followers,
                callback=self.user_followers_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables)}
            )

        for follower in followers_info:
            item = InstaparserFollowersItem(
                userid=follower.get('pk'),
                username=follower.get('username'),
                fullname=follower.get('full_name'),
                photo=follower.get('profile_pic_url'),
                following_id=None,
                follower_id=user_id
            )
            yield item

    def user_following_parse(self, response: HtmlResponse, username, user_id, variables):
        j_data = response.json()
        following_info = j_data.get('users')
        max_id = j_data.get('next_max_id')
        if max_id:
            variables['max_id'] = max_id
            url_following = f'{self.inst_graphql_link}{user_id}/following/?{urlencode(variables)}'

            yield response.follow(
                url_following,
                callback=self.user_followers_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables)}
            )

        for following in following_info:
            item = InstaparserFollowersItem(
                userid=following.get('pk'),
                username=following.get('username'),
                fullname=following.get('full_name'),
                photo=following.get('profile_pic_url'),
                following_id = user_id,
                follower_id=None
            )
            yield item

    def fetch_csrf_token(self, text):
        ''' Get csrf-token for auth '''
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')

    def fetch_user_id(self, text, username):
        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')
