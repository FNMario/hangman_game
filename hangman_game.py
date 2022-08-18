import os
import random

def enter_letter():
    key_pressed = input('\nIngresa una letra: ').upper()
    try:
        if not key_pressed.isupper():
            raise ValueError('Debe ingresar una letra')
        if len(key_pressed) > 1:
            raise Exception('No se puede ingresar mas de una letra')
        return key_pressed
    except ValueError as ve:
        print(ve)
        return False
    except Exception as ex:
        print(ex)
        return False

def print_screen(word, lives=8):
    os.system('clear')
    print_lines = []
    print_lines.extend(range(5))
    print_lines.extend(range((8 - lives)*12 + 15, (8 - lives)*12 + 27))

    with open(r'./files/imagenes.txt', 'r', encoding='UTF-8') as f:
        for l,line in enumerate(f):
            if l in print_lines:
                print(line, end='')

    print('                                                 ', end='')
    for letter in word:
        print(letter, end=' ')


def print_end(win):
    if win:
        os.system('clear')
        print_lines = range(5, 10)
    else:
        print_lines = range(10, 15)
    print('\n')
    with open(r'./files/imagenes.txt', 'r', encoding='UTF-8') as f:
        for l,line in enumerate(f):
            if l in print_lines:
                print(line, end='')
    print('\n')

def run():
    entered_leters = []
    lives = 8

    with open(r'./files/data.txt', 'r', encoding='UTF-8') as f:
        word_list = [words.strip().upper() for words in f]

    random.seed()   # Initialize the random number generator
    choosen_word = random.choice(word_list)
    word = ['_' for letter in choosen_word]

    while True:

        print_screen(word, lives)

        while True:
            letter = enter_letter()
            try: 
                entered_leters.index(letter)
                print('Esa letra ya fue ingresada')
            except ValueError:
                if letter:
                    entered_leters.append(letter)
                    break

        guess = False
        for pos, char in enumerate(choosen_word):
            if (char == letter):
                word[pos] = char
                guess = True
        
        if not guess:
            lives -= 1
            if lives == 0:
                print_screen(word, lives)
                print_end(win = False)
                break
        else:
            if word.count('_') == 0:
                print_end(win = True)
                break

    
    print('La palabra era: ' + choosen_word.capitalize())

if __name__ == '__main__':
    run()