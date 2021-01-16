# https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    output = ''
    for letter in message: 
        if letter.isalpha():
            if letter == letter.upper():
                num = 65
            else: 
                num = 97
            letter = chr(((ord(letter)-num + 13) % 26) + num)  
        output = output + letter
    return output 