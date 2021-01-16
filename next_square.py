# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if (sq ** 0.5).is_integer():
        return ((sq ** 0.5)+1) ** 2 
    else:
        return -1