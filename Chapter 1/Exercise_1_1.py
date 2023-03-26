# SICP Exercise 1.1
# Author: Jack Peters

# Below is a sequence of expressions.
# What is the result printed by the interpreter in response to each expression?
# Assume that the sequence is to be evaluated in the order in which it is presented.

print(10)
# prints 10

print(5 + 3 + 4)
# prints 12

print(9 - 1)
# prints 8

print(6 / 2)
# prints 3.0

print(2 * 4 + (4 - 6))
# prints 6

a = 3; print(a)
# prints 3

b = a + 1; print(b)
# prints 4

print(a + b + a * b)
# prints 19

a = b; print(a)
# prints 4

if b > a and b < a * b:
  print(b)
else:
  print(a)
# prints 4

if a == 4:
    print(6)
elif b == 4:
    print(6 + 7 + a)
else:
    print(25)
# prints 6

if b > a:
    print(2 + b)
else:
    print(2 + a)
# prints 6

if a > b:
    print(a * (a + 1))
elif a < b:
    print(b * (a + 1))
else:
    print(-1 * (a + 1))
# prints -5
