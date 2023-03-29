# Exercise 1.4
# Author: Jack Peters

# Observe that out model of evaluation allows for combinations
# whose operators are compound expressions. Use this observation
# to describe the behavior of the following procedure:
#
# (define (a-plus-abs-b a b)
#   ((if (> b 0) + -) a b))

def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    else:
        return a - b

print(a_plus_abs_b(3, 2))
# prints 5

print(a_plus_abs_b(3, -2))
# prints 5
