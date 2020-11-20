#!/usr/bin/env python
'''
This is a test module without a __main__ statement.
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


# Here is where we execute the main code, although there is no __main__ statement.
a = 4
print(f"Is {a} an even number? {even(a)}")
