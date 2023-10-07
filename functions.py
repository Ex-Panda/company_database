import requests


def get_company(tuple_id_company):
    list_company = []
    for id_company in tuple_id_company:
        url_hh_ru_company = f"https://api.hh.ru/employers/{id_company}"
        res = requests.get(url=url_hh_ru_company).json()
        list_company.append([res['id'], res['name'], res['vacancies_url']])
    return list_company


def get_vacancy(list_company):
    list_vacancy = []

    for i in list_company:
        res = requests.get(url=i[2]).json()

        for company in res['items']:
            if company['salary'] is not None and company['salary']['from'] is None and company['salary']['to'] is not None:
                list_vacancy.append([company["name"], None, company['salary']['to'],
                                     company['salary']['currency'], company['alternate_url'], company["employer"]["id"]])
            elif company['salary'] is not None and company['salary']['to'] is None and company['salary']['from'] is not None:
                list_vacancy.append([company["name"], company['salary']['from'], None,
                                     company['salary']['currency'], company['alternate_url'], company["employer"]["id"]])
            elif company['salary'] is None:
                list_vacancy.append([company["name"], None, None, None, company['alternate_url'], company["employer"]["id"]])
            else:
                list_vacancy.append([company["name"], company['salary']['from'], company['salary']['to'],
                                     company['salary']['currency'], company['alternate_url'], company["employer"]["id"]])
    return list_vacancy
