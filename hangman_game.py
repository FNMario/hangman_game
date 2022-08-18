import os
import random

pressed_keys = []

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

def run():
    with open(r'./files/data.txt', 'r', encoding='UTF-8') as f:
        word_list = [words.strip().upper() for words in f]

    random.seed()   # Initialize the random number generator
    choosen_word = random.choice(word_list)
    word = ['_' for letter in choosen_word]

    while word.count('_'):
        os.system('clear')
        print(choosen_word)
        print('Adivina la palabra!')
        for letter in word:
            print(letter, end=' ')
        
        while True:
            letter = enter_letter()
            if letter:
                break

        for pos, char in enumerate(choosen_word):
            if (char == letter):
                word[pos] = char
        letter = False

    os.system('clear')
    print('¡CORRECT! The word was: ' + choosen_word)

if __name__ == '__main__':
    run()