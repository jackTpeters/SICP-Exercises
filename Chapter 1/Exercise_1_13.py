# Exercise 1.13
# Author: Jack Peters

# Prove that Fib(n) is the closest integer to
# phi^n / 5, where phi = (1 + sqrt(5)) / 2. Hint: Let
# psi = (1 - sqrt(5)) / 2. Use induction and the defintion
# of the Fibonacci numbers (see Section 1.2.2) to prove
# that Fib(n) = (phi^n - psi^n) / sqrt(5).
#
# Let phi = (1 + sqrt(5)) / 2 and psi = (1 - sqrt(5)) / 2.
# Notice that (phi^0 - psi^0) / sqrt(5) = 0 = Fib(0). Also
# notice that  (phi - psi) / sqrt(5) = 1 = Fib(1). Thus the
# base case holds. Assume that n <= k holds. Consider
# n = k + 1. We have (phi^(k+1) - psi^(k+1)) / sqrt(5)
# = (phi^(k-1) * phi^2 - psi^(k-1) * psi^2) / sqrt(5). Notice
# that phi^2 = ((1 + sqrt(5)) / 2)^2 = (6 + 2 * sqrt(5)) / 4
# = (3 + sqrt(5)) / 2 = 1 + phi. Similarly, psi^2
# = ((1 - sqrt(5)) / 2)^2 = (6 - 2 * sqrt(5)) / 4
# = (3 - sqrt(5)) / 2 = 1 + psi. Thus, we have
# (phi^(k-1) * phi^2 - psi^(k-1) * psi^2) / sqrt(5)
# = (phi^(k-1) * (1 + phi) - psi^(k-1) * (1 + psi)) / sqrt(5)
# = (phi^k - psi^k) / sqrt(5) + (phi^(k-1) - psi^(k-1)) / sqrt(5)
# = Fib(k) + F(k - 1) = Fib(k + 1).
