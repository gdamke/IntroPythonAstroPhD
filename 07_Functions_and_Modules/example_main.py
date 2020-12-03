#!/usr/bin/env python

'''
This is a test module with a __main__ statement.
'''

def odd(x):
    '''
    Evaluate if a number is odd.
    '''
    
    return int(x) % 2 == 1

def even(x):
    '''
    Evaluate if a number is odd.
    '''
    
    return int(x) % 2 == 0

def _another_function(x):
    print(x)

def __a_func(x):
    print(x)

print(__name__)
if __name__ == "__main__":
    # Here is where we execute the main code
    b = 4
    print(f"Is {b} an even number? {even(b)}")
