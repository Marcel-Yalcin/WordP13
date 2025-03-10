'''
Program: WordP13

Description: Functions that implement the game WordP13 (similar to the game 
Wordle). They load words from specified files after checking each one, assign
a random index for a list of words, update which letters the user has guessed
and evaluate how close the user is to guessing the chosen word.
'''
import random

def load_words(filename):
    '''Returns a list of words found in the file: filename. If a word doesn't
    have the same amount of characters as the first word in the file or has
    non-alphabetic characters, the function returns False instead.'''
    file = open(filename, "r")
    file_list = []
    first_line = True
    # adds each line to an empty list
    for line in file:
        # removes the newline \n
        word = line.strip()
        if first_line == True:
            length = len(word)
        # checks if there are any bad characters and that the word is the length of the file's first word.
        if len(word) != length or not word.isalpha():
            return False
        file_list.append(word)
        first_line = False
    
    file.close()
        
    return file_list

def choose_word(word_list):
    '''Takes a list of words as a parameter. If the list is empty, False
    is returned. Otherwise, a random integer representing an index in the list
    is returned.'''
    if len(word_list) == 0:
        return False 
    return random.randint(0,len(word_list)-1)

def update_letters(letters, target, guess):
    '''Takes a list of 26 booleans (letters), where each index represents a 
    letter in the alphabet, the chosen word (target) and the user's guess. 
    If there are matching characters in target and guess, the 
    corresponding index in letters is changed to True.'''
    for i in range(0,len(guess)-1):
        # uses ASCII values of characters; works for lowercase only here
        letters_index = ord(guess[i]) - 97 # -97 since ord("a")=97
        # if guess and target characters are the same
        if guess[i] == target[i]:
            letters[letters_index] = True
        else:
            letters[letters_index] = False
    return letters

def score_guess(guess, target, words):
    '''Takes the user's guess, the word and a list of acceptable words
    as parameters. Runs a loop to check each character in the user's guess
    and outputs accordingly. Evaluation is case insensitive.'''
    # checks if guess is correct length and in the word list
    if len(guess) != len(target) or not guess.lower() in words:
        return False
    
    result = ""
    for i in range(len(guess)):
        # letter is correct and in the correct place
        if guess[i].lower() == target[i]:
            result += "*"
        # letter is correct but in wrong place
        elif guess[i].lower() in target:
            result += "?"
        # letter is wrong
        else:
            result += "_"
    
    return result