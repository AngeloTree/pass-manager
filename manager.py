from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

# PostgreSQL DB #
DB_HOST = "localhost"
DB_NAME = "sandbox"
DB_USER = "angelo"
DB_PASS = "abc123"

def get_connection():
   conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
   return conn

def login():
    with get_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(f"""
                CREATE TABLE manager (
                    id serial PRIMARY KEY,
                    site VARCHAR (255),
                    username VARCHAR (255),
                    password VARCHAR (255)
                    )
                    """)
            print('done')


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
        login()

            
