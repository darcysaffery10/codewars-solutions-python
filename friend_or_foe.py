# https://www.codewars.com/kata/55b42574ff091733d900002f

def friend(x): 
#     friends = x.split(" ")
    output = []
    for y in x:    
        if len(y) == 4:
            output.append(y) 
    return output
        