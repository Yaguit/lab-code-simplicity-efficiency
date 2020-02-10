"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import string

def StringGenerator():
    a = int(input('Minimum length: '))
    b = int(input('Maximum length: '))
    n = int(input('How many strings do you want? '))
    list_of_strings = []
    
    for i in range(0,n):
        length = random.randrange(a,b)
        char = string.ascii_lowercase + string.digits
        list_of_strings.append(''.join(random.choice (char) for i in range(length)))
        
    print(list_of_strings)

StringGenerator()