from dotenv import load_dotenv
import os

load_dotenv('.env')

# Create a dotenv file later on to hide information
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
