from dataclasses import dataclass
from sys import breakpointhook
from unittest.mock import NonCallableMagicMock
from dotenv import load_dotenv
import os
from h11 import Data
import psycopg2
import psycopg2.extras
import logging

logger = logging.getLogger(__name__)

# PostgreSQL DB #
DB_HOST = "localhost"
DB_NAME = "sandbox"
DB_USER = "angelo"
DB_PASS = "abc123"


class Database:
    def __init__(self):
        self = self

    def get_connection(self):
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        return conn


class Manager(Database):
    def create_data(self):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                try:
                    cursor.execute(f"""
                        CREATE TABLE manager (
                            id serial PRIMARY KEY,
                            site VARCHAR (255),
                            username VARCHAR (255),
                            password VARCHAR (255)
                            )
                            """)
                    #main_menu()
                except psycopg2.errors.DuplicateTable as e:
                    logger.exception(e)
                    #main_menu()=

    def create_info(self):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                site = input('Site name: ')
                site_user = input('User name for that site: ')
                site_pass = input('Password for that site: ')
                cursor.execute(f"INSERT INTO manager (site, username, password) VALUES ('{site}', '{site_user}', '{site_pass}')")
                print('Info created')


# A While loop to enter the correct password to enter the DataBase which then sends you to database_creation()
load_dotenv('.env')
secret_pass = os.getenv('MANAGER_PASS_WORD')
login_tries = 3
pass_word = None
current_user = None

def main_menu():
    menu_choice = input("Would you like to create, read, update, or delete? (Type one of the following - C,R,U,D) Or E to Exit: ")
    return menu_choice.lower()

while True:
    if pass_word == secret_pass:
        if current_user == None:
            print('created ONLY')
            current_user = Manager()
            current_user.create_data()
        choice_return = main_menu()
        if choice_return == 'c':
            print('c')
            current_user.create_info()
            continue
        elif choice_return == 'r':
            print('test')
            print('r')
            continue
        elif choice_return == 'u':
            print('u')
            continue
        elif choice_return == 'd':
            print('r')
            continue
        elif choice_return == 'e':
            print('e')
            break
    elif pass_word != secret_pass:
        pass_word = input('Please Enter your Pass: ')
        if pass_word != secret_pass:
            login_tries -= 1
            print(f'You have {login_tries} attempts left.')
            if login_tries == 0:
                print('PROGRAM SHUTTING DOWN')
                break
            continue

       