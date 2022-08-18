import random
from secrets import choice

def run():
    with open(r'./files/data.txt', 'r', encoding='UTF-8') as f:
        word_list = [words for words in f]

    random.seed()   # Initialize the random number generator
    choosen_word = choice(word_list)
    print(choosen_word)

if __name__ == '__main__':
    run()