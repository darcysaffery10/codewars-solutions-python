# https://www.codewars.com/kata/536c00e21da4dc0a0700128b 

def get_villain_name(birthdate): 
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    # your code here
    
    date = str(birthdate).split(' ')[0]  
    month = int(date.split('-')[1]) # 5
    day = int(date.split('-')[2][-1]) # 5 
    
    first_name = first[month-1]
    last_name = last[day]
    return first_name + ' ' + last_name

