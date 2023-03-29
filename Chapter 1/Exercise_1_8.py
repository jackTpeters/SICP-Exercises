# Exercise 1.8
# Author: Jack Peters

# Newton’s method for cube roots is based on
# the fact that if y is an approximation to the cube root of x,
# then a better approximation is given by the value
#
# (x / y**2 + 2 * y) / 3
#
# Use this formula to implement a cube-root procedure anal-
# ogous to the square-root procedure. (In Section 1.3.4 we will
# see how to implement Newton’s method in general as an
# abstraction of these square-root and cube-root procedures.)

def cube_root(x):
    def cube_root_iter(y, x):
        tolerance = 0.00001
        square = lambda x : x * x
        cube = lambda x : x * x * x
        imprv_guess = lambda y, x : (x / square(y) + 2 * y) / 3
        if abs(cube(y) - x) < tolerance:
            return y
        else:
            return cube_root_iter(imprv_guess(y, x), x)
    return cube_root_iter(1, x)

print(cube_root(8))
print(cube_root(-8))
print(cube_root(-27))
