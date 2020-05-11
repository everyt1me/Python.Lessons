import mysql.connector
import requests
from lib.settings import COVID19_URL
if __name__ == "__main__":
    db_manager


class db_manager:
    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID19")
        self.__cursor.execute("USE COVID19")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS global(id INT AUTO_INCREMENT PRIMARY KEY, NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT(10))")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS countries(id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(12), Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT(10), Date DATE)")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Update data\n2. Search by country name\n3. Search by country code\n0. Exit\n"))
            if choice == 1:
                answer = self.__update_covid_data()
            elif choice == 2:
                answer = self.__search_by_country_name()
            elif choice == 3:
                answer = self.__search_by_country_code()
            elif choice == 0:
                exit = True
                print("Exit")
            else:
                print("Wrong choice")

    def __update_covid_data(self):
        covid_data = requests.get(COVID19_URL)
        covid_data = covid_data.json()

        self.__cursor.execute("DELETE FROM global")
        global_sql = "INSERT INTO global (NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered) VALUES(%s, %s, %s, %s, %s, %s)"
        global_values = (covid_data['Global']["NewConfirmed"],
                         covid_data['Global']["TotalConfirmed"], covid_data['Global']["NewDeaths"], covid_data['Global']["TotalDeaths"], covid_data['Global']["NewRecovered"], covid_data['Global']["TotalRecovered"])
        self.__cursor.execute("DELETE FROM countries")
        self.__cursor.execute(global_sql, global_values)
        for item in covid_data['Countries']:
            countries_sql = "INSERT INTO countries (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            countries_values = item["Country"], item["CountryCode"], item["Slug"], item["NewConfirmed"], item[
                "TotalConfirmed"], item["NewDeaths"], item["TotalDeaths"], item["NewRecovered"], item["TotalRecovered"], item["Date"]
            self.__cursor.execute(countries_sql, countries_values)

            print("Country COVID19 info:\n" + "Country:", countries_values[0], "\n" + "Country code:", countries_values[1], "\n" + "Slug:", countries_values[2], "\n" + "New confirmed:", countries_values[3], "\n" + "Total confirmed:", countries_values[4],
                  "\n" + "New deaths:", countries_values[5], "\n" + "Total death:", countries_values[6], "\n" + "New recovered:", countries_values[7], "\n" + "Total recovered:", countries_values[8], "\n" + "Last data update:", countries_values[9], "\n")

        print("GLOBAL COVID19 info:\n" + "New confirmed:", global_values[0], "\n" + "Total global confirmed:", global_values[1], "\n" + "New deaths global:", global_values[2],
              "\n" + "Total global death:", global_values[3], "\n" + "New global recovered:", global_values[4], "\n" + "Total global recovered:", global_values[5], "\n")
        self.__db.commit()

    def __search_by_country_name(self):
        answer = input(
            "To search COVID19 info by country, please enter country name:\n===> ")
        self.__cursor.execute(
            "SELECT * FROM `countries` WHERE Country = '" + answer + "'")
        result = self.__cursor.fetchone()
        if result != None:
            print("COVID19 info by country name:\n" + "Country:", result[1], "\n" + "Country code:", result[2], "\n" + "New confirmed:", result[4], "\n" + "Total confirmed:", result[5], "\n" +
                  "New deaths:", result[6], "\n" + "Total death:", result[7], "\n" + "New recovered:", result[8], "\n" + "Total recovered:", result[9], "\n" + "Last data update:", result[10], "\n")
        elif result == None:
            return print("\nWrong country name!\n")

    def __search_by_country_code(self):
        answer = input(
            "To search COVID19 info by country code, please enter country code name:\n===> ")
        self.__cursor.execute(
            "SELECT * FROM `countries` WHERE CountryCode = '" + answer + "'")
        result = self.__cursor.fetchone()
        if result != None:
            print("COVID19 info by country code:\n" + "Country:", result[1], "\n" + "Country code:", result[2], "\n" + "New confirmed:", result[4], "\n" + "Total confirmed:", result[5], "\n" +
                  "New Deaths:", result[6], "\n" + "Total death:", result[7], "\n" + "New recovered:", result[8], "\n" + "Total recovered:", result[9], "\n" + "Last data update:", result[10], "\n")
        elif result == None:
            return print("\nWrong country code!\n")
