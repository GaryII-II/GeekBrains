# https://gb.ru/lessons/184649/homework
# Scrap vacancies from hh.ru (vacancy title is inputted) by few pages (number of pages is inputted)
# https://spb.hh.ru/search/vacancy?clusters=true&area=2&ored_clusters=true&enable_snippets=true&salary=&text=Java+developer

import requests
import pprint
from bs4 import BeautifulSoup
import pandas as pd

results_list = []

# Surf vacancies on 1 HH page by  the number
def look_hh_page(page_num):
    vacancy = 'Java developer'
    url = 'https://spb.hh.ru'
    params = {'clusters': 'true',
              'area': '2', 'ored_clusters': 'true', 'enable_snippets': 'true',
              'salary': '',
              'text': 'Java%2Bdeveloper',
              'page': str(page_num)}
    headers = {'Accept': '*/*',
               # Chrome
               # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

               # Edge
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43/'}

    response = requests.get(url + '/search/vacancy', params=params, headers=headers)
    if not response.ok:
        print(f'Request error: {response.status_code}')
        pass

    dom = BeautifulSoup(response.text, 'html.parser')

    vacancies = dom.find_all('div', attrs={'class': 'vacancy-serp-item'})

    if len(vacancies) <= 0:
        print('Empty list of vacancies')
        pass

    for item in vacancies:
        vacancy_data = {}
        vacancy_base = item.find('a', attrs={'class': 'bloko-link'})
        vacancy_data['job_title'] = vacancy_base.text
        vacancy_data['job_link'] = vacancy_base['href']

        firm_data = item.find('a', attrs={'class': 'bloko-link bloko-link_secondary'})
        firm_site = ''
        firm = ''
        if firm_data:
            firm_site = url + firm_data['href']
            firm = firm_data.text
        vacancy_data['firm'] = firm
        vacancy_data['firm_site'] = firm_site
        firm_data = item.find(attrs={'data-qa': 'vacancy-serp__vacancy-address'})
        firm_address = ''
        if firm_data:
            firm_address = firm_data.text
        vacancy_data['firm_address'] = firm_address

        try:
            salary = item.find(attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
            if not salary:
                continue

            currency = salary.text.split()[-1]
            rest = salary.text.split()[:-1:]
            if 'от' in rest: rest.remove('от')
            rest = ['–' if item == 'до' else item for item in rest]
            val = "".join(rest)
            triade = val.partition('–')

            vacancy_data['salary_min'] = None if not triade[0] else int(triade[0])
            vacancy_data['salary_max'] = None if not triade[2] else int(triade[2])
            vacancy_data['salary_currency'] = currency

        except:
            vacancy_data['salary_min'] = None
            vacancy_data['salary_max'] = None
            vacancy_data['salary_currency'] = None

        results_list.append(vacancy_data)


pages = input('Input number of HeadHunter pages to look through: ')
if not pages.isdigit():
    print('Incorrect value type. Look through 1 page')
    pages = 1
else:
    pages = int(pages)

for page_num in range (0, pages):
    look_hh_page(page_num+1)

# Fill result file
print(f'Look through {pages} pages\n')
pprint.pprint(results_list)

result_pd = pd.DataFrame(results_list)
result_pd.to_csv('c:/Temp/lesson2.csv', sep='\t')

