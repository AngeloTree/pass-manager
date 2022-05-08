from dataclasses import dataclass
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras
import logging

logger = logging.getLogger(__name__)

## WORKING ON PROGRAM REVAMP USING OOP

# PostgreSQL DB #
DB_HOST = "localhost"
DB_NAME = "sandbox"
DB_USER = "angelo"
DB_PASS = "abc123"

def get_connection():
   conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
   return conn


# Checks to see if you already have a DataBase created and if not it creates one and either or it sends you to the main_menu()
def database_creation():
    with get_connection() as conn:
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
                print('DataBase Created.')
                main_menu()
            except psycopg2.errors.DuplicateTable as e:
                logger.exception(e)
                print('DataBase already created.')
                main_menu()


# Create a row in the DataBase
def create_info():
    with get_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            site = input('Site name: ')
            site_user = input('User name for that site: ')
            site_pass = input('Password for that site: ')
            cursor.execute(f"INSERT INTO manager (site, username, password) VALUES ('{site}', '{site_user}', '{site_pass}')")
            print('Info created')


# This is the main_menu where you choose one of the CRUD abilities with user input
def main_menu():
    while True:
        crud_choice = input('Would you like to create, read, update, or delete? (Type one of the following - C,R,U,D): ')



# A While loop to enter the correct password to enter the DataBase which then sends you to database_creation()
load_dotenv('.env')
secret_pass = os.getenv('MANAGER_PASS_WORD')
login_tries = 3

while True:
    pass_word = input('Please Enter your Pass: ')
    if pass_word != secret_pass:
        login_tries -= 1
        print(f'You have {login_tries} attempts left.')
        if login_tries == 0:
            print('PROGRAM SHUTTING DOWN')
            break
        continue
    elif pass_word == secret_pass:
        print('Correct!')
        database_creation()

            
