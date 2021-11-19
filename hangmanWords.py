from nltk.corpus import words
import random

def getRandomWord():
    wordList = words.words()    
    return random.choice(wordList)

def wordtoBlanks(word):
    blanks = ""
    for letter in word:
        blanks = blanks + '_'
    return blanks

def printwordBlanks(blanks): 
    newBlanks = ""
    for letter in blanks:
        newBlanks = newBlanks + (letter + ' ')
    return newBlanks

def updateLetters(guess, word, blanks):
    newBlanks = ""
    for i in range(0, len(word)):
        if guess == word[i]: 
            newBlanks = newBlanks + word[i]
        else:
            newBlanks = newBlanks + blanks[i]
    return newBlanks
