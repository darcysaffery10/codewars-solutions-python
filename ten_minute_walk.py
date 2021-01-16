# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) == 10:
        if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
            return True 
        else:
            return False
    else: 
        return False 