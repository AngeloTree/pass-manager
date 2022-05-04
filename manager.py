
secret_pass = '123'  # Create a dotenv file later on to hide information

while True:
    pass_word = input('Please Enter your Pass: ')

    if pass_word != '123':
        print('That is not the password. Please try again..')
        continue
    elif pass_word == secret_pass:
        print('Correct!')
