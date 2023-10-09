import os
import psycopg2

from dbmanager import DBManager
from functions import get_company, get_vacancy

# ID 10 интересующих компаний
tuple_id_company = ('4888751', '2101345', '5178281', '3551849', '8644487', '1149418', '4955824', '9373043', '4614421', '2769379')

list_company = get_company(tuple_id_company)
list_vacancy_company = get_vacancy(list_company)

try:
    with psycopg2.connect(
        host="localhost",
        database="company",
        user="postgres",
        password="pokemon007"
    ) as conn:
        with conn.cursor() as cur:
            cur.executemany('INSERT INTO company VALUES (%s, %s, %s)', list_company)
            cur.executemany('INSERT INTO vacancy VALUES (%s, %s, %s, %s, %s, %s)', list_vacancy_company)
finally:
    conn.close()

a = DBManager()
print(a.get_companies_and_vacancies_count())
print(a.get_all_vacancies())
print(a.get_avg_salary())
print(a.get_vacancies_with_higher_salary())
print(a.get_vacancies_with_keyword('Python'))