# https://gb.ru/lessons/184650/homework
# MongoDB.
# Task1. Function fill_jobs to add only new vacancies/products to DB
# Task2. Function find_jobs to find jobs with a salary more the specifies amount

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import pprint


# Reading list of vacancies from Head Hunter
def get_vacancies(job_title):
    import requests
    from bs4 import BeautifulSoup

    url = 'https://spb.hh.ru'
    params = {'clusters': 'true',
              'area': '2', 'ored_clusters': 'true', 'enable_snippets': 'true',
              'salary': '',
              'text': job_title.replace(' ', '%2B')}
    headers = {'Accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

    response = requests.get(url + '/search/vacancy', params=params, headers=headers)
    if not response.ok:
        print(f'Request error: {response.status_code}')
        pass

    dom = BeautifulSoup(response.text, 'html.parser')

    vacancies = dom.find_all('div', attrs={'class': 'vacancy-serp-item'})
    hh_jobs_list = []

    if len(vacancies) <= 0:
        print('Empty list of vacancies')
        return hh_jobs_list

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
            triad = val.partition('–')

            vacancy_data['salary_min'] = None if not triad[0] else int(triad[0])
            vacancy_data['salary_max'] = None if not triad[2] else int(triad[2])
            vacancy_data['salary_currency'] = currency

        except:
            vacancy_data['salary_min'] = None
            vacancy_data['salary_max'] = None
            vacancy_data['salary_currency'] = None

        # Generate record id with the hash
        vacancy_data['_id'] = hash(frozenset(vacancy_data.items()))
        hh_jobs_list.append(vacancy_data)

    pprint.pprint(hh_jobs_list)
    return hh_jobs_list


# Fill database wih jobs
def fill_jobs(collection, job_title):

    # Get current vacancies from HeadHunter
    res = get_vacancies(job_title)
    if len(res) <= 0:
        print('No new jobs found')

    # Insert to the collection
    added = 0
    for job in res:
        try:
            # Consider that unique ID will avoid adding the same vacancy
            collection.insert_one(job)
            added = added + 1
        except DuplicateKeyError as e:
            print(f'Duplicated record found: ' + job['job_title'])

    print(f'\nAdded {added} vacancies!\n')

    for job in collection.find({}):
        pprint.pprint(job)


# Finds jobs with a salary more the specifies amount
def find_jobs(collection, salary_floor):

    items = 0
    for job in collection.find({'$or': [{'salary_min': {'$gte': salary_floor}},
                                        {'salary_max': {'$gt': salary_floor}}]}):
        items = items + 1
        pprint.pprint(job)

    print(f'\nFound {items}  records!\n')


# ===================================================
# Connecting to Database to store the data
client = MongoClient("127.0.0.1", 27017)
db = client['HeadHunter']
vacancies_list = db.vacancies

job_name = input('Which job are you looking for (e.g.: Java Developer)?: ')
if len(job_name) > 0:
    fill_jobs(vacancies_list, job_name)

salary_limit = input('Which salary limit are you looking for?: ')
result = salary_limit.isdigit()
if not salary_limit.isdigit():
    print('Incorrect value type. Input number, please')
else:
    find_jobs(vacancies_list, int(salary_limit))
