# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132


def validate_pin(pin):
        if pin.isdigit() and ((len(str(pin)) == 4) or (len(str(pin)) == 6)):
            return True
        else: 
            return False