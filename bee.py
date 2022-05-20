# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 10:00:27 2022

@author: luanp
"""

import random
import pickle


file = open('wordlist.txt', 'rb')
WORDLIST = pickle.load(file)

file = open('words7.txt', 'rb')
WORDS_7 = pickle.load(file)


def get_letters(wordlist):
    """
    Finds random word with 7 letters, returns unique letters and one special letter.
    ---
    param wordlist: list of words
    ---
    Returns:
    list of 7 letters and one special letter
    """
    word = random.choice(wordlist)
    if len(set(word)) != 7:
        print("Word should have 7 unique letters!")
        raise TypeError
    print(word)
    letter_list = [c for c in set(word)]
    special_letter = random.choice(letter_list)
    return letter_list, special_letter

#_letter_list = get_letters(WORDS_7)
#_special_letter = random.choice(_letter_list)

def to_str(letter_list):
    s = ""
    for c in letter_list:
        s += c.upper() + " "
    return s.strip()

def check_score(input_str, wordlist, letterlist, special_letter, min_lett=4):
    """
    """
    if special_letter not in input_str:
        return f"Word must contain letter {special_letter.upper()}!", 0
    if len(input_str) < min_lett:
        return f"Word must have at least {min_lett} letters!", 0
    if len(set(input_str) - set(letterlist)) != 0:
        return "Letter not in list!", 0
    if input_str not in wordlist:
        return "Word not found!", 0
    if len(input_str) == min_lett:
        return "", 1
    if len(set(input_str)) == len(letterlist):
        return "Pangram!", 15
    return "", len(input_str)

def get_solutions(wordlist, letter_list, special_letter, min_lett=4):
    solutions = [w for w in wordlist if len(w) >= min_lett and special_letter in w and len(set(w) - set(letter_list)) == 0]
    return solutions

def terminal_game(wordlist, letter_list):
    points = 0
    used_words = []
    while True:
        word = input("Type in a word: ").lower()
        if word in used_words:
            print("Word already has been used!")
        else:
            used_words.append(word)
            points += check_score(word, wordlist, letter_list)
        print(points)
        
if __name__ == "__main__":
    letters, special_letter = get_letters(WORDS_7)
    sol = get_solutions(WORDLIST, letters, special_letter)
    print(letters, special_letter, sol)