"""
1.Write a program that prints the numbers from 1 to 100. But for multiples of three print “Tec” instead of the number and for the multiples of five print “tona”.
2. For numbers which are multiples of both three and five, print “Tectona”.
3. xtend the "Array" class in Javascript with a new method that calculates and returns the sum of the Array's items (you can assume all of the items are numbers).
"""


import numpy as np

# No 2
def print_numbers():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print ('Tectona')
        elif i % 3 == 0:
            print ('Tec')
        elif i % 5 == 0:
            print ('tona')
        else:
            print (i)

            
# No 3
# in JS: const sum = (x) => x.reduce((total, current) => total + current, 0);
def sum_array(arr):
    # answer to No 3 in Python
    return np.array(arr).sum()
            
            
if __name__ == '__main__':
    print_numbers()

    