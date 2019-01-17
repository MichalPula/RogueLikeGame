import os
import roguelike_game


def display_screen(filename):
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def menu_select():
    while True:
        os.system('clear')
        display_screen('start_screen.txt')
        answer = input("Choose option: ")

        if answer == '1':
            break

        elif answer == '2':
            os.system('clear')
            display_screen('howtoplay.txt')
            input('\nPress enter key to go back')

        elif answer == '3':
            os.system('clear')
            display_screen('about_creators.txt')
            input('\nPress enter key to go back')


def hero_creation():
    os.system('clear')
    hero = ['@', '#', '&']
    display_screen('intro.txt')
    appearance = input('Select your hero: @, # or & ')
    for symbol in hero:
        if symbol is appearance:
            return symbol


