def f(x, y, z):
    return -(x**2) - (y**2) - (z**2) + 2*x*y - y*z + 3*z

print(f(-3, 3, 0))
print(f(10, 10, 10))
print(f(-10, -10, -10))
print(f(-100, -100, 100))
print(f(-1000, -1000, 1000))