import string
import random

def main():
    print(r'''
       *Secure Password Generator*

                .-""-.
               / .--. \
              / /    \ \
              | |    | |
              | |.-""-.|
             ///`.::::.`\
            ||| ::/  \:: ;
            ||; ::\__/:: ;
             \\\ '::::' /
              `=':-..-'`

1) Generate secure password (8 characters length by default)
2) Choose the number of characters you want
3) Quit program''')

    user_choice = int(input('Enter an option: '))

    while user_choice != 1 and user_choice != 2 and user_choice != 3:
        user_choice = int(input('Enter a valid option: '))

    if user_choice == 1:
        option_1()
    elif user_choice == 2:
        option_2()
    elif user_choice == 3:
        option_3()


def option_1():
    strings_alphabet = string.ascii_letters
    strings_digits = string.digits
    strings_symbols = string.punctuation
    all_strings = strings_alphabet + strings_digits + strings_symbols

                                                   # .sample --> (value, specified number of values I want)
    secure_combo = random.sample(all_strings, 8)
                                   # --> *value, sep = '' --> Very useful to print from lists in a clean way
    print(*secure_combo, sep='')

    print()
    user_choice = input('Try again? (y/n): ')
    user_choice.lower()
    while user_choice != 'y' and user_choice != 'n':
        user_choice = input('Try again? (y/n): ')

    while user_choice == 'y':
        secure_combo = random.sample(all_strings, 8)
        print(*secure_combo, sep='')
        user_choice = input('Try again? (y/n): ')

    if user_choice == 'n':
        print()
        print('Very well!')
        print('**********')

    main()

def option_2():
    strings_alphabet = string.ascii_letters
    strings_digits = string.digits
    strings_symbols = string.punctuation
    all_strings = strings_alphabet + strings_digits + strings_symbols
    chosen_characters = int(input('How many characters?: '))

    secure_combo = random.sample(all_strings, chosen_characters)
    print(*secure_combo, sep='')

    print()
    user_choice = input('Try again? (y/n): ')
    user_choice.lower()
    while user_choice != 'y' and user_choice != 'n':
        user_choice = input('Try again? (y/n): ')

    while user_choice == 'y':
        secure_combo = random.sample(all_strings, chosen_characters)
        print(*secure_combo, sep='')
        user_choice = input('Try again? (y/n): ')

    if user_choice == 'n':
        print()
        print('Very well!')
        print('**********')

    main()


def option_3():
    print()
    print('**********')
    print('''Thank you for using 6ER\'s: 
Secure Password Generator!''')
    print('See you soon!')
    print('**********')
    quit()


main()