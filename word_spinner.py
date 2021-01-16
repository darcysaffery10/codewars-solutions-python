# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    words = sentence.split(" ")
    output = ""
    for word in words:
        if len(word) > 4:
            word = word[::-1]
        output = output + word + " "       
    return output[:-1]