#!/usr/bin/env python
# coding: utf-8


from words import words
from alphabets import alphabets
import random

def randomWord():
    random_word = random.choice(words)
    
    return random_word.upper()

def wordLetters():
    word_list = []
    word_list[:0] = randomWord()
    return word_list


def randomizedLetters():
    word = wordLetters()
    randomized_word = word.copy()
    for i in range(5):
        randomized_word.append(random.choice(alphabets))
    
    return [word,randomized_word]

def missingWord(word_length):
    namess = '_'*word_length
    return '.'.join(namess)

def hangman():
    word_choice = randomizedLetters()
    word_length = len(word_choice[0])
    word = '.'.join(word_choice[0])
    missing_word = missingWord(word_length)
    randomized_word = random.sample(word_choice[1], len(word_choice[1]))
    print('Welcome to the game of Hangman built by Mfanafuthi \nThis game of hangman has no rules!! ')
    print(f"From the following letters '{' '.join(randomized_word)}', choose a letter!\n\n\n")
    print(f"Here is your clue:{missing_word}")
    print(word)
    input_letter = 'lutho'
    while input_letter:
        input_letter = input(f"Letter:").upper()
        if input_letter != '':
            missing_word = missing_word.replace('_',input_letter,1)
    return[word,missing_word]   
    
def hangman_game():
    compare_words = hangman()
    if (compare_words[0]==compare_words[1]):
        print('You guessed the word right!!')
    else:
        print('You are not good with words are you?')


