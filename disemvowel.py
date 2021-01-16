# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string): 
    newWord = string
    vowels = ['a', 'e', 'i', 'o', 'u']  
    for letter in string:
        if letter.lower() in vowels:
            newWord = newWord.replace(letter, '')
    return newWord 