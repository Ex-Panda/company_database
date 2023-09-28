import os
import psycopg2

api_key_hh = api_key = os.getenv('API_SuperJob')

#ID 10 интересующих компаний
tuple_id_company = ('4888751', '2101345', '5178281', '3551849', '8644487', '1149418', '4955824', '9373043', '4614421', '2769379')

#Почитай документацию и получи список вакансий по каждой компаний
pass


try:
    with psycopg2.connect(
        host="localhost",
        database="company_database",
        user="postgres",
        password="pokemon007"
    ) as conn:
        with conn.cursor() as cur:
            pass
finally:
    pass
