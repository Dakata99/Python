#!/bin/python3

# Find the numbers in the interval [begin, end] containing only once (= 1) <number> in themselves
# Ex.: 5, 15, 25, ..., 501, ...
def once(number, begin, end):
    numbers = list()
    number = str(number)

    for i in range(begin, end + 1, 1):
        number_as_str = str(i)
        
        if number_as_str.count(number) == 1:
            numbers.append(i)

    return numbers

# Find the numbers in the interval [begin, end] containing at least once (>= 1) <number> in themselves
# Ex.: 5, 15, 55, ..., 505, 555, ...
def at_least_once(number, begin, end):
    numbers = list()
    number = str(number)

    for i in range(begin, end + 1, 1):
        number_as_str = str(i)
        
        if number_as_str.count(number) >= 1:
            numbers.append(i)

    return numbers
    
# Find the numbers in the interval [begin, end] containing at most once (<= 1) <number> in themselves
# Ex.: [0 - 9], 15, 25, ..., 45, 54, 56, ..., 65, ..., 500, ...
def at_most_once(number, begin, end):
    numbers = list()
    number = str(number)

    for i in range(begin, end + 1, 1):
        number_as_str = str(i)
        
        if number_as_str.count(number) <= 1:
            numbers.append(i)

    return numbers

# Driver code
if __name__ == '__main__':
    l = once(5, 0, 1000)
    print(l)
    print(len(l))

    l = at_least_once(5, 0, 1000)
    print(l)
    print(len(l))

    l = at_most_once(5, 0, 1000)
    print(l)
    print(len(l))