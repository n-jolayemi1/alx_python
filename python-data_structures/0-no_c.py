#!/usr/bin/python3

def no_c(my_string):
    cee = 'c'
    new_string = ''
    for i in my_string:
        result = (cee != i) and (cee.upper() != i)
        if result :
            new_string += i
    return new_string