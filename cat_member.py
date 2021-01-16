# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(data):
    output = []
    for sublist in data:
        if sublist[0] >= 55 and sublist[1] > 7:
            output.append("Senior")
        else: output.append("Open")    
    return output