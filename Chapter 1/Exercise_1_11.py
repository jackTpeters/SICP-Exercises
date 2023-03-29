# Exercise 1.11
# Author: Jack Peters

# A function f is defined by the rule that
#
# f(n) = {n if n < 3, f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3) if n >= 3}
#
# Write a procedure that computes f by means of a recursive
# process. Write a procedure that computes f by means of an
# iterative process.

# Recursive
def f_rec(n):
    if n < 3:
        return n
    else:
        return f_rec(n - 1) + 2 * f_rec(n - 2) + 3 * f_rec(n - 3)

# Iterative
def f_iter(n):
    iter = lambda x, y, z, i : 3 * x + 2 * y + z if n == i else iter(y, z, 3 * x + 2 * y + z, i + 1)
    if n < 3:
        return n
    else:
        return iter(0, 1, 2, 3)

print(f_rec(10))
print(f_iter(10))
