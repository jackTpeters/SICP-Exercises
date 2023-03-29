# Exercise 1.12
# Author: Jack Peters

# The following pattern of numbers is called
# Pascal's triangle:
#
#                 1
#             1       1
#         1       2       1
#     1       3       3       1
# 1       4       6       4       1
#               . . .
#
# The numbers at the edge of the triangle are all 1, and each
# number inside the triangle is the sum of the two numbers
# above it. Write a procedure that computes elements of
# Pascal’s triangle by means of a recursive process.

def pascal(n, k):
    # n = row
    # k = column
    if k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

print(pascal(4, 2))
