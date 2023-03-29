# Exercise 1.7
# Author: Jack Peters

# The "good-enough?" test used in computing
# square roots will not be very effective for finding the square
# roots of very small numbers. Also, in real computers, arith-
# metic operations are almost always performed with lim-
# ited precision. This makes our test inadequate for very large
# numbers. Explain these statements, with examples showing
# how the test fails for small and large numbers. An alterna-
# tive strategy for implementing "good-enough?" is to watch
# how guess changes from one iteration to the next and to
# stop when the change is a very small fraction of the guess.
# Design a square-root procedure that uses this kind of end
# test. Does this work better for small and large numbers?

# Computer arithmetic operations report an answer to a certain
# number of bits. This is done to maintain resonable memory
# availability levels. Since very large numbers (and very small
# numbers) require many bits to store them, operations with these
# numbers will usually produce numbers which also require many
# bits to store them. Opeartions will produce numbers which will
# eventually reach their bit capacity and so require a rounding
# of the resulting number, meaning a decrease in precsion. If
# the number is large enough (or small enough), this could
# greatly change the number. Thus, an algorithm which would be
# testing for, or making, slight changes in a number, would not
# work for adequately large or small numbers.

import sys
sys.setrecursionlimit(100000)

def square_root(x):
    def square_root_iter(guess, x):
        tolerance = 0.000000000000000000001
        square = lambda x : x * x
        imprv_guess = lambda guess, x : (x / guess + guess) / 2
        if abs(square(guess) - x) < tolerance:
            return guess
        else:
            return square_root_iter(imprv_guess(guess, x), x)
    return square_root_iter(1, x)

print(square_root(1e-123456789))
print(square_root(2e123456789))

# A strategy for which we stop iterating our guess
# once the change between guesses is very small, better suits large
# numbers because the tolerence is quickly reached.
#
# Something to note is that Python has an easier time working with
# smaller numbers than larger numbers. Observe the examples above.
