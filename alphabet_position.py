# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    return ' '.join([str(ord(letter)-96) for letter in text.lower() if letter.isalpha()])