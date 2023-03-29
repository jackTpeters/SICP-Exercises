# Exercise 1.3
# Author: Jack Peters

# Define a procedure that takes three numbers as arguments and returns
# the sum of the squares of the two larger numbers.

def square_sum_large(a, b, c):
    square_sum = lambda x, y : x**2 + y**2
    if a >= c and b >= c:
        return square_sum(a, b)
    elif a >= b and c >= b:
        return square_sum(a, c)
    else:
        return square_sum(b, c)

print(square_sum_large(3, 2, 2))
# prints 13

print(square_sum_large(2, 2, 2))
# prints 8

print(square_sum_large(3, 2, 4))
# prints 25
