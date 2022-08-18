import os
import random

pressed_keys = []

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
        key_pressed = input('\nIngresa una letra: ').upper()
        
        for pos, char in enumerate(choosen_word):
            if (char == key_pressed):
                word[pos] = char

    os.system('clear')
    print('¡CORRECT! The word was: ' + choosen_word)

if __name__ == '__main__':
    run()