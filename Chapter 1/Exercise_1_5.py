# Exercise 1.5
# Author: Jack Peters

# Ben Bitdiddle has invented a test to determine whether
# the interpreter he is faced with is using applicative-order
# evaluation or normal-order evaluation. He defines the
# following two procedures:
#
# (define (p) (p))
# (define (test x y)
#   (if (= x 0) 0 y))
#
# Then he evaluates the expression:
#
# (test 0 (p))
#
# What behavior will Ben observe with an interpreter that uses
# applicative-order evaluation? What behavior will he observe
# with an interpreter that uses normal-order evaluation? Explain
# your answer. (Assume that the evaluation rule for the special
# form "if" is the same whether the interpreter is using normal
# or applicative order: The predicate expression is evaluated
# first, and the result determines whether to evaluate the
# consequent or the alternative expression.)

# When using applicative-order evaluation, Ben will receive an
# error. This is because (define (p) (p)) is not a valid procedure
# and must be evaluated when input as a parameter to "test".
# When using normal-order evaluation however, Ben will receive 0.
# This is because in normal-order the invalid procedure
# (define (p) (p)) will be evaluated when it is encountered which
# would be in the alternative expression. Since the alternative
# expression is never encountered with an input of x = 0 in "test",
# no error will be thrown.
