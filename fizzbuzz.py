# https://www.codewars.com/kata/5300901726d12b80e8000498

def fizzbuzz(n):
    new_list = []
    for number in range(1, n+1):
        if (number % 3 == 0) & (number % 5 == 0):
            new_list.append('FizzBuzz')
        elif number % 3 == 0:
            new_list.append('Fizz')
        elif number % 5 == 0:
            new_list.append('Buzz')
        else:    
            new_list.append(number)
    return(new_list)