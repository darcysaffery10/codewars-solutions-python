# https://www.codewars.com/kata/57e2afb6e108c01da000026e

def expression_out(exp):
    dictionary = { '+':   ' Plus ',
  '-':   ' Minus ',
  '*':   ' Times ',
  '/':   ' Divided By ',  
  '**':  ' To The Power Of ',
  '=':   ' Equals ',
  '!=':  ' Does Not Equal ',
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three', 
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',
    '10' : 'Ten'}

    new_string = ''
    count = 0
    for n in exp.split():
        if count == 1:
            if n in [str(num) for num in range(1,11)]:
                return 'That\'s not an operator!'
        try: 
            new_string = new_string + dictionary[n]
        except: 
            return 'That\'s not an operator!'
        count += 1
    return new_string 