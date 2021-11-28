# List of repositories of GitHub user

import requests
from requests.auth import HTTPBasicAuth

# GitHub user name
user = 'Add_Name_here'

# GitHub access token for the user
token = 'Add_token_here'

# GitHub API url
url = 'https://api.github.com/users/{0}/repos'.format(user)

response = requests.get(url,  auth=HTTPBasicAuth(user, token))

repos_Data = (response.json())

print(f'Repositories for user {user}')
[print(f"{items['name']}") for items in repos_Data]

