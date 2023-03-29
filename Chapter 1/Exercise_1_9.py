# Exercise 1.9
# Author: Jack Peters

# Each of the following two procedures defines
# a method for adding two positive integers in terms of the
# procedures inc, which increments its argument by 1, and
# dec, which decrements its argument by 1.
#
# (define (+ a b)
#     (if (= a 0) b (inc (+ (dec a) b))))
# (define (+ a b)
#     (if (= a 0) b (+ (dec a) (inc b))))
#
# Using the substitution model, illustrate the process gener-
# ated by each procedure in evaluating (+ 4 5). Are these
# processes iterative or recursive?

# For the first procedure:
#
# (define (+ a b)
#     (if (= a 0) b (inc (+ (dec a) b))))
#
# we have:
#
# (+ 4 5)
# (inc (+ (dec 4) 5))
# (inc (+ 3 5))
# (inc (inc (+ (dec 3) 5)))
# (inc (inc (+ 2 5)))
# (inc (inc (inc (+ (dec 2) 5))))
# (inc (inc (inc (+ 1 5))))
# (inc (inc (inc (inc (+ (dec 1) 5)))))
# (inc (inc (inc (inc (+ 0 5)))))
# (inc (inc (inc (inc 5))))
# (inc (inc (inc 6)))
# (inc (inc 7))
# (inc 8)
# 9
#
# For the second procedure:
#
# (define (+ a b)
#     (if (= a 0) b (+ (dec a) (inc b))))
#
# we have:
#
# (+ 4 5)
# (+ (dec 4) (inc 5))
# (+ 3 6)
# (+ (dec 3) (inc 6))
# (+ 2 7)
# (+ (dec 2) (inc 7))
# (+ 1 8)
# (+ (dec 1) (inc 8))
# (+ 0 9)
# 9
#
# We see that the first procedure is recursive with time O(x)
# and space O(x). The second procedure is iterative with time
# O(x) and space O(1). Thus the second procedure is more efficient.
