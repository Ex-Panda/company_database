import psycopg2


class DBManager:

    def connect_database(self, sql):
        list_sql = []
        try:
            with psycopg2.connect(
                    host="localhost",
                    database="company",
                    user="postgres",
                    password="pokemon007"
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    list_sql = cur.fetchall()
        finally:
            conn.close()

        return list_sql

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        return self.connect_database("""SELECT name_company, COUNT(name_vacancy) FROM company
                                     INNER JOIN vacancy ON company.id_company = vacancy.id_employer
                                     GROUP BY name_company""")

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию"""
        return self.connect_database("""SELECT name_company, name_vacancy, salary_from, salary_to, alternate_url
                                        FROM vacancy
                                        INNER JOIN company ON company.id_company = vacancy.id_employer""")

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        return self.connect_database("""SELECT (AVG(salary_from) + AVG(salary_to)) / 2 AS salary_avg 
                                        FROM vacancy""")

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        return self.connect_database("""SELECT name_vacancy
                                        FROM vacancy
                                        WHERE (salary_from + salary_to) / 2 >
                                        (SELECT (AVG(salary_from) + AVG(salary_to)) / 2 AS salary_avg 
                                        FROM vacancy)""")

    def get_vacancies_with_keyword(self, word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        return self.connect_database(f"""SELECT name_vacancy
                                        FROM vacancy
                                        WHERE name_vacancy LIKE '%{word}%'""")

