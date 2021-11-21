# Use any open API requiring an authorization
import requests
import json

from requests.auth import HTTPBasicAuth

# NewsAPI access token. Refer to https://www.thenewsapi.com/documentation
token = 'Add_Access_Token_Here'

# Top stories
url = f'https://api.thenewsapi.com/v1/news/top?api_token={token}&locale=us&limit=3'

response = requests.get(url)
if not response.ok:
    print('Error')
    pass
repos_Data = response.json()
articles = repos_Data['data']

with open('task2_response.json', 'w') as f:
    json.dump(repos_Data, f)

with open('task2_TopStories.txt', 'w') as f:
    f.write(f'Top 3 stories from The News')
    [f.write(f"{items['title']}\n") for items in articles]

