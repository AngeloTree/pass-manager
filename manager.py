from dataclasses import dataclass
from sys import breakpointhook
from unittest.mock import NonCallableMagicMock
from dotenv import load_dotenv
import os
from h11 import Data
import psycopg2
import psycopg2.extras
import logging
import sys

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

    def read_info(self):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                site = input('Type in a site you like to view the login info to:  ')
                cursor.execute(f"SELECT * FROM manager WHERE site = '{site}'")
                b = cursor.fetchall()
                print(f'Site: {site}, User: {b[0][2]}, Pass: {b[0][3]}')
                # site_user = cursor.fetchone()['username']
                # site_pass = cursor.fetchone()['password']
                # print(f"Site: {site}, User: {site_user}, Pass: {site_pass}")

    def update_info(self):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                site = input('Type in a site you like to change the login info to:  ')
                choice_input = input('Do you want to update the username or password (u/p): ')
                if choice_input == 'u':
                    updated_user = input('Type the user in: ')
                    cursor.execute(f"UPDATE manager SET username = '{updated_user}' WHERE site = '{site}'")
                elif choice_input == 'p':
                    updated_password = input('Type the password in: ')
                    cursor.execute(f"UPDATE manager SET password = '{updated_password}' WHERE site = '{site}'")
                else:
                    print("That doesn't exist.")

    def delete_info(self):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                site = input('Type in a site of the information you like to delete: ')
                cursor.execute(f"DELETE FROM manager WHERE site = '{site}'")

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
            crud_input = {
                'c' : current_user.create_info,
                'r' : current_user.read_info,
                'u' : current_user.update_info,
                'd' : current_user.delete_info   
                }
        choice_return = main_menu()
        for x, y in crud_input.items():
            if choice_return == x:
                crud_input[x]()
            elif choice_return == 'e':
                sys.exit("PROGRAM SHUTTING DOWN")
    elif pass_word != secret_pass:
        pass_word = input('Please Enter your Pass: ')
        if pass_word != secret_pass:
            login_tries -= 1
            print(f'You have {login_tries} attempts left.')
            if login_tries == 0:
                print('PROGRAM SHUTTING DOWN')
                break
            continue

       